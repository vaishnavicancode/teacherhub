import { NextRequest, NextResponse } from 'next/server'
import { MongoClient } from 'mongodb'
import { v4 as uuidv4 } from 'uuid'

const client = new MongoClient(process.env.MONGO_URL)
const dbName = process.env.DB_NAME || 'teacherhub'

async function connectToDatabase() {
  try {
    await client.connect()
    return client.db(dbName)
  } catch (error) {
    console.error('Database connection error:', error)
    throw error
  }
}

export async function GET(request, { params }) {
  const path = params.path?.join('/') || ''
  
  try {
    const db = await connectToDatabase()
    
    // Get all teachers
    if (path === 'teachers') {
      const teachers = await db.collection('teachers').find({}).toArray()
      return NextResponse.json({ teachers })
    }
    
    // Get all students
    if (path === 'students') {
      const students = await db.collection('students').find({}).toArray()
      return NextResponse.json({ students })
    }
    
    // Get single teacher
    if (path.startsWith('teachers/')) {
      const teacherId = path.split('/')[1]
      const teacher = await db.collection('teachers').findOne({ id: teacherId })
      if (!teacher) {
        return NextResponse.json({ error: 'Teacher not found' }, { status: 404 })
      }
      return NextResponse.json({ teacher })
    }
    
    // Get single student
    if (path.startsWith('students/')) {
      const studentId = path.split('/')[1]
      const student = await db.collection('students').findOne({ id: studentId })
      if (!student) {
        return NextResponse.json({ error: 'Student not found' }, { status: 404 })
      }
      return NextResponse.json({ student })
    }
    
    return NextResponse.json({ error: 'Endpoint not found' }, { status: 404 })
  } catch (error) {
    console.error('API Error:', error)
    return NextResponse.json({ error: 'Internal server error' }, { status: 500 })
  }
}

export async function POST(request, { params }) {
  const path = params.path?.join('/') || ''
  
  try {
    const db = await connectToDatabase()
    const body = await request.json()
    
    // Create new teacher
    if (path === 'teachers') {
      const teacher = {
        id: uuidv4(),
        name: body.name,
        email: body.email,
        phone: body.phone,
        department: body.department,
        subject: body.subject,
        hireDate: body.hireDate,
        salary: body.salary,
        qualification: body.qualification,
        experience: body.experience,
        createdAt: new Date(),
        updatedAt: new Date()
      }
      
      await db.collection('teachers').insertOne(teacher)
      return NextResponse.json({ teacher })
    }
    
    // Create new student
    if (path === 'students') {
      const student = {
        id: uuidv4(),
        name: body.name,
        email: body.email,
        phone: body.phone,
        grade: body.grade,
        section: body.section,
        teacherId: body.teacherId,
        parentName: body.parentName,
        parentPhone: body.parentPhone,
        createdAt: new Date(),
        updatedAt: new Date()
      }
      
      await db.collection('students').insertOne(student)
      return NextResponse.json({ student })
    }
    
    return NextResponse.json({ error: 'Endpoint not found' }, { status: 404 })
  } catch (error) {
    console.error('API Error:', error)
    return NextResponse.json({ error: 'Internal server error' }, { status: 500 })
  }
}

export async function PUT(request, { params }) {
  const path = params.path?.join('/') || ''
  
  try {
    const db = await connectToDatabase()
    const body = await request.json()
    
    // Update teacher
    if (path.startsWith('teachers/')) {
      const teacherId = path.split('/')[1]
      const updateData = {
        ...body,
        updatedAt: new Date()
      }
      
      const result = await db.collection('teachers').updateOne(
        { id: teacherId },
        { $set: updateData }
      )
      
      if (result.matchedCount === 0) {
        return NextResponse.json({ error: 'Teacher not found' }, { status: 404 })
      }
      
      const teacher = await db.collection('teachers').findOne({ id: teacherId })
      return NextResponse.json({ teacher })
    }
    
    // Update student
    if (path.startsWith('students/')) {
      const studentId = path.split('/')[1]
      const updateData = {
        ...body,
        updatedAt: new Date()
      }
      
      const result = await db.collection('students').updateOne(
        { id: studentId },
        { $set: updateData }
      )
      
      if (result.matchedCount === 0) {
        return NextResponse.json({ error: 'Student not found' }, { status: 404 })
      }
      
      const student = await db.collection('students').findOne({ id: studentId })
      return NextResponse.json({ student })
    }
    
    return NextResponse.json({ error: 'Endpoint not found' }, { status: 404 })
  } catch (error) {
    console.error('API Error:', error)
    return NextResponse.json({ error: 'Internal server error' }, { status: 500 })
  }
}

export async function DELETE(request, { params }) {
  const path = params.path?.join('/') || ''
  
  try {
    const db = await connectToDatabase()
    
    // Delete teacher
    if (path.startsWith('teachers/')) {
      const teacherId = path.split('/')[1]
      const result = await db.collection('teachers').deleteOne({ id: teacherId })
      
      if (result.deletedCount === 0) {
        return NextResponse.json({ error: 'Teacher not found' }, { status: 404 })
      }
      
      return NextResponse.json({ message: 'Teacher deleted successfully' })
    }
    
    // Delete student
    if (path.startsWith('students/')) {
      const studentId = path.split('/')[1]
      const result = await db.collection('students').deleteOne({ id: studentId })
      
      if (result.deletedCount === 0) {
        return NextResponse.json({ error: 'Student not found' }, { status: 404 })
      }
      
      return NextResponse.json({ message: 'Student deleted successfully' })
    }
    
    return NextResponse.json({ error: 'Endpoint not found' }, { status: 404 })
  } catch (error) {
    console.error('API Error:', error)
    return NextResponse.json({ error: 'Internal server error' }, { status: 500 })
  }
}