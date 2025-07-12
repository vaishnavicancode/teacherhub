# TeacherHub - Modern Teacher Management System

A comprehensive, modern teacher management interface built with Next.js, TypeScript, and Tailwind CSS. This application provides an intuitive platform for managing teachers, students, and educational data with a focus on user experience and responsive design.

## 🚀 Features

### Core Functionality
- **Teacher Management**: Complete CRUD operations for teacher profiles
- **Student Management**: Student enrollment and assignment to teachers
- **Dashboard Analytics**: Real-time statistics and performance metrics
- **Modern UI/UX**: Clean, responsive design with dark/light mode support
- **Search & Filter**: Advanced filtering capabilities for teachers and students
- **Department Management**: Organize teachers by departments and subjects

### Technical Highlights
- **Next.js 14**: Latest React framework with App Router
- **TypeScript**: Type-safe development experience
- **Tailwind CSS**: Utility-first styling with shadcn/ui components
- **MongoDB**: Robust database with proper indexing
- **Responsive Design**: Mobile-first approach with modern UI patterns
- **Dark/Light Mode**: Theme switching with system preference detection

## 📋 Prerequisites

- Node.js 18.0 or higher
- MongoDB 4.4 or higher
- npm or yarn package manager

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd teacherhub
   ```

2. **Install dependencies**
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Set up environment variables**
   Create a `.env.local` file in the root directory:
   ```env
   MONGO_URL=mongodb://localhost:27017
   DB_NAME=teacherhub_db
   NEXT_PUBLIC_BASE_URL=http://localhost:3000
   ```

4. **Start MongoDB**
   Make sure MongoDB is running on your system:
   ```bash
   # macOS (with Homebrew)
   brew services start mongodb-community
   
   # Ubuntu/Debian
   sudo systemctl start mongod
   
   # Windows
   net start MongoDB
   ```

5. **Run the development server**
   ```bash
   npm run dev
   # or
   yarn dev
   ```

6. **Open your browser**
   Navigate to [http://localhost:3000](http://localhost:3000)

## 🏗️ Project Structure

```
teacherhub/
├── app/
│   ├── api/
│   │   └── [[...path]]/
│   │       └── route.js          # API routes for CRUD operations
│   ├── globals.css               # Global styles
│   ├── layout.js                 # Root layout component
│   └── page.js                   # Main application page
├── components/
│   └── ui/                       # shadcn/ui components
├── lib/
│   └── utils.js                  # Utility functions
├── public/                       # Static assets
├── .env.local                    # Environment variables
├── next.config.js               # Next.js configuration
├── tailwind.config.js           # Tailwind CSS configuration
└── package.json                 # Project dependencies
```

## 🎨 Design System

The application uses a consistent design system built with:
- **shadcn/ui**: Pre-built, accessible components
- **Tailwind CSS**: Utility-first CSS framework
- **Lucide React**: Beautiful, customizable icons
- **Inter Font**: Modern typography

### Color Palette
- **Primary**: Modern blue tones for actions and highlights
- **Secondary**: Subtle grays for secondary elements
- **Accent**: Complementary colors for status indicators
- **Background**: Dynamic light/dark theme support

## 📊 API Endpoints

### Teachers
- `GET /api/teachers` - Get all teachers
- `GET /api/teachers/{id}` - Get teacher by ID
- `POST /api/teachers` - Create new teacher
- `PUT /api/teachers/{id}` - Update teacher
- `DELETE /api/teachers/{id}` - Delete teacher

### Students
- `GET /api/students` - Get all students
- `GET /api/students/{id}` - Get student by ID
- `POST /api/students` - Create new student
- `PUT /api/students/{id}` - Update student
- `DELETE /api/students/{id}` - Delete student

### Data Models

#### Teacher
```typescript
{
  id: string;
  name: string;
  email: string;
  phone: string;
  department: string;
  subject: string;
  hireDate: string;
  salary: number;
  qualification: string;
  experience: number;
  createdAt: Date;
  updatedAt: Date;
}
```

#### Student
```typescript
{
  id: string;
  name: string;
  email: string;
  phone: string;
  grade: string;
  section: string;
  teacherId: string;
  parentName: string;
  parentPhone: string;
  createdAt: Date;
  updatedAt: Date;
}
```

## 🧪 Testing

The application includes comprehensive backend API testing:

```bash
# Run backend tests
python backend_test.py

# Test coverage includes:
# - All CRUD operations
# - Database connectivity
# - Error handling
# - Data validation
# - Edge cases
```

## 🚀 Deployment

### Vercel (Recommended)
1. Push your code to GitHub
2. Connect your repository to Vercel
3. Set environment variables in Vercel dashboard
4. Deploy automatically

### Other Platforms
The application can be deployed on any platform that supports Next.js:
- Netlify
- Railway
- Render
- AWS Amplify
- DigitalOcean App Platform

## 📱 Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## 🔧 Configuration

### Environment Variables
- `MONGO_URL`: MongoDB connection string
- `DB_NAME`: Database name
- `NEXT_PUBLIC_BASE_URL`: Application base URL

### Customization
- **Themes**: Modify `tailwind.config.js` for custom colors
- **Components**: Extend shadcn/ui components in `components/ui/`
- **Database**: Adjust MongoDB models in API routes

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Next.js](https://nextjs.org/) for the amazing React framework
- [Tailwind CSS](https://tailwindcss.com/) for the utility-first CSS framework
- [shadcn/ui](https://ui.shadcn.com/) for the beautiful component library
- [MongoDB](https://www.mongodb.com/) for the flexible database solution
- [Vercel](https://vercel.com/) for the deployment platform

## 📞 Support

For support, please open an issue in the GitHub repository or contact the development team.
video link: https://drive.google.com/file/d/1MJ6QluOsoKScghrt9Ijuf0v4cIPp29gs/view?usp=sharing
---

**Built with ❤️ using modern web technologies**
