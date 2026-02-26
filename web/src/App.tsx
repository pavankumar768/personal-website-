import Footer from './components/layout/Footer'
import Navbar from './components/layout/Navbar'
import AboutSection from './components/sections/AboutSection'
import AchievementsSection from './components/sections/AchievementsSection'
import CertificatesSection from './components/sections/CertificatesSection'
import ContactSection from './components/sections/ContactSection'
import HeroSection from './components/sections/HeroSection'
import ProjectsSection from './components/sections/ProjectsSection'
import SkillsSection from './components/sections/SkillsSection'

export default function App() {
  return (
    <div className="min-h-screen bg-white text-slate-900">
      <Navbar />
      <main>
        <HeroSection />
        <AboutSection />
        <SkillsSection />
        <ProjectsSection />
        <CertificatesSection />
        <AchievementsSection />
        <ContactSection />
      </main>
      <Footer />
    </div>
  )
}
