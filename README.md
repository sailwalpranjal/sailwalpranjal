    #include <iostream>
    #include <string>
    #include <vector>

    class DataScientist {
    private:
    	std::string name = "Pranjal Sailwal";
    	std::string title = "Data Scientist & Machine Learning Engineer";
	    std::string location = "Exploring the World of Data 📊";
    	std::vector<std::string> skills = {
	    	"Data Analysis", "Machine Learning", "Statistical Analysis",
	    	"Data Visualization", "Python", "R Programming",
	    	"Deep Learning", "Natural Language Processing", "Big Data Technologies",
    		"Predictive Modeling", "Data Mining", "Time Series Analysis",
		    "Feature Engineering", "Data Preprocessing", "Database Management",
    		"Data Warehousing", "Data Storytelling", "A/B Testing",
		    "Hadoop Ecosystem", "Spark", "TensorFlow", "Scikit-Learn"
	    };
	    std::string aboutMe = "I'm passionate about extracting insights from data and building predictive models that drive informed decisions. My journey in data science involves exploring vast datasets, creating machine learning models, and telling compelling data-driven stories.";

    public:
    	void introduce() {
    		std::cout << "\t👋 Hello, I'm " << name << ", a " << title << " based in " << location << "." << std::endl;
	    	std::cout << "\t" << aboutMe << std::endl;
    	}

	    void skillsAndPurpose() {
		    std::cout << "\t🛠️ Here are some of my skills and what they mean:" << std::endl;
    		std::cout << "\t - Data Analysis: Uncovering valuable insights from data to help organizations make informed decisions." << std::endl;
	    	std::cout << "\t - Machine Learning: Teaching computers to learn from data and make predictions or automate tasks." << std::endl;
		    std::cout << "\t - Statistical Analysis: Applying statistical methods to analyze data distributions and relationships." << std::endl;
    		std::cout << "\t - Data Visualization: Creating visual representations of data to make complex information more understandable." << std::endl;
	    	std::cout << "\t - Python: Using Python programming language for data analysis, machine learning, and more." << std::endl;
		    std::cout << "\t - R Programming: Leveraging R for statistical analysis, data visualization, and reporting." << std::endl;
		    std::cout << "\t - Deep Learning: Building advanced machine learning models for tasks like image and speech recognition." << std::endl;
		    std::cout << "\t - Natural Language Processing: Teaching computers to understand and interact with human language." << std::endl;
		    std::cout << "\t - Big Data Technologies: Handling and processing large volumes of data efficiently." << std::endl;
		    std::cout << "\t - Predictive Modeling: Using data to predict future outcomes, aiding in forecasting and planning." << std::endl;
		    std::cout << "\t - Data Mining: Discovering patterns and knowledge from large datasets." << std::endl;
		    std::cout << "\t - Time Series Analysis: Analyzing time-ordered data for forecasting and trend analysis." << std::endl;
		    std::cout << "\t - Feature Engineering: Creating meaningful input variables for machine learning models." << std::endl;
		    std::cout << "\t - Data Preprocessing: Cleaning and preparing data for analysis and modeling." << std::endl;
		    std::cout << "\t - Database Management: Managing and querying databases to extract valuable information." << std::endl;
	    	std::cout << "\t - Data Warehousing: Storing and managing data from various sources for analysis." << std::endl;
		    std::cout << "\t - Data Storytelling: Communicating data-driven insights in a compelling and understandable manner." << std::endl;
		    std::cout << "\t - A/B Testing: Comparing different versions of a product to determine which performs better." << std::endl;
    		std::cout << "\t - Hadoop Ecosystem: Tools for distributed storage and processing of big data." << std::endl;
    		std::cout << "\t - Spark: Processing large datasets with speed and efficiency using Apache Spark." << std::endl;
	    	std::cout << "\t - TensorFlow: Building and training machine learning models with the TensorFlow framework." << std::endl;
	    	std::cout << "\t - Scikit-Learn: Utilizing the Scikit-Learn library for machine learning tasks." << std::endl;
	    }

	    void projects() {
		    std::cout << "\t🚀 Here are some of my projects showcasing these skills:" << std::endl;
		    std::cout << "\t1. Sales Prediction Model:" << std::endl;
		    std::cout << "\t   - Description: Developed a machine learning model to predict future sales trends based on historical data. This helped optimize inventory management and reduce costs." << std::endl;
		    std::cout << "\t2. Image Recognition Application:" << std::endl;
		    std::cout << "\t   - Description: Created an application that identifies objects in images using deep learning. This has applications in security and content tagging." << std::endl;
		    std::cout << "\t3. Customer Sentiment Analysis Tool:" << std::endl;
		    std::cout << "\t   - Description: Built a tool that analyzes customer feedback to understand sentiment. This assists businesses in improving customer experience and product development." << std::endl;
	    	std::cout << "\t4. Big Data Analytics Platform:" << std::endl;
	    	std::cout << "\t   - Description: Developed a data analytics platform to process and analyze large datasets using Hadoop and Spark. This enables efficient data-driven decision-making for organizations." << std::endl;
	    	std::cout << "\t5. A/B Testing Dashboard:" << std::endl;
	    	std::cout << "\t   - Description: Designed an A/B testing dashboard for marketing campaigns, helping teams evaluate the effectiveness of different strategies and make data-backed decisions." << std::endl;
    		std::cout << "\t6. Data Visualization Dashboard:" << std::endl;
    		std::cout << "\t   - Description: Developed an interactive data visualization dashboard for business performance analysis. This facilitates easy understanding of key metrics and trends." << std::endl;
    	}

    	void finalProject() {
    		std::cout << "\t🌟 For my ultimate project, I combined all these skills in a comprehensive Data Science Challenge:" << std::endl;
    		std::cout << "\t - Project: Customer Churn Prediction for a Telecom Company" << std::endl;
    		std::cout << "\t   - Description: Conducted an end-to-end data science project to predict customer churn for a telecom company. Collected and preprocessed large-scale customer data, engineered relevant features, built machine learning models for prediction, and presented results through interactive data visualizations." << std::endl;
    		std::cout << "\t   - Impact: By identifying potential churn, the company reduced customer attrition, resulting in increased revenue and improved customer satisfaction." << std::endl;
    	}
    };

    int main() {

    	DataScientist pranjal;

    	pranjal.introduce();
    	std::cout << std::endl;
    	pranjal.skillsAndPurpose();
    	std::cout << std::endl;
    	pranjal.projects();
    	std::cout << std::endl;
    	pranjal.finalProject();

    	std::cout << "\t🚀 Ready to explore the world of data science? Let's make data-driven insights a reality!" << std::endl;

    	return 0;
    }
