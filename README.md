    #include <iostream>
    #include <string>
    #include <vector>

    class SoftwareEngineer {
    private:
        std::string name = "Pranjal Sailwal";
        std::string title = "Full-Stack Alchemist";
        std::string location = "Everywhere 🌍";
        std::vector<std::string> skills = {
            "JavaScript", "Python", "React", "Node.js", "SQL",
            "Machine Learning", "Docker", "AWS", "CI/CD"
        };
        std::vector<std::string> passions = {
            "Open Source", "Problem Solving", "Continuous Learning",
            "Tech Ethics", "Space Exploration"
        };
        std::string motto = "Turning coffee ☕ into code 💻";

    public:
        void introduce() {
            std::cout << "🚀 **Greetings, fellow digital voyagers!** I am " << name << ", a maestro of algorithms and an architect of digital realms." << std::endl;
            std::cout << "My journey as a " << title << " has been nothing short of spectacular." << std::endl;
            std::cout << "With an unwavering command over languages like JavaScript and Python, I sculpt interactive web and mobile ecosystems with ease." << std::endl;
            std::cout << "My code is the harmonious blend of artistry and functionality, and it's all fueled by the elixir of life – caffeine!" << std::endl;
        }

        void skillsAndPassions() {
            std::cout << "🛠️ **My toolkit is adorned with the following languages and tools:** " << std::endl;
            for (const std::string& skill : skills) {
                std::cout << " - " << skill << std::endl;
            }

            std::cout << "💡 **My passions ignite the spark of creativity:** " << std::endl;
            for (const std::string& passion : passions) {
                std::cout << " - " << passion << std::endl;
            }
        }

        void mission() {
            std::cout << "🌟 **In my quest through the digital cosmos,** I have realized that technology is a catalyst for transformation." << std::endl;
            std::cout << "My purpose is to channel this power for the betterment of humanity, always striving to uphold tech ethics." << std::endl;
            std::cout << "Open source is my creed, and I thrive in the crucible of challenges, emerging as a relentless problem solver." << std::endl;
            std::cout << "Let us unite, for in collaboration lies the path to crafting extraordinary solutions." << std::endl;
        }

        void exploreTheStars() {
            std::cout << "🌌 **When I'm not in the code-sculpting trance,** you'll find me gazing at the stars, dreaming of space exploration." << std::endl;
            std::cout << "The final frontier beckons, and I believe that technology can propel us to new cosmic horizons." << std::endl;
            std::cout << "Join me on this cosmic journey, and let's push the boundaries of human knowledge together." << std::endl;
        }
    };

    int main() {
        
        SoftwareEngineer pranjal;
        
        pranjal.introduce();
        std::cout << std::endl;
        pranjal.skillsAndPassions();
        std::cout << std::endl;
        pranjal.mission();
        std::cout << std::endl;
        pranjal.exploreTheStars();
        
        std::cout << "🚀 **Let's embark on a coding odyssey and reach for the stars together!**" << std::endl;
        
        return 0;
    }
