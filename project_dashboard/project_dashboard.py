import streamlit as st


def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-vector/white-abstract-background_23-2148806276.jpg?w=1380&t=st=1704616465~exp=1704617065~hmac=9435b372ddd03aee15f44dd4f43c0833adfb9a0a817ed2d1f7a6a52c2b3c3c24");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


def papers_page():
    add_bg_from_url()

    # Custom CSS for better formatting
    st.markdown("""
    <style>
    .big-font {
        font-size: 50px !important;
        font-weight: bold;
        color: #1E90FF;
        text-align: center;
    }
    .section-title {
        font-size: 30px !important;
        font-weight: bold;
        color: #4B0082;
        margin-top: 30px;
        margin-bottom: 20px;
    }
    .paper-title {
        font-size: 22px !important;
        font-weight: bold;
        color: #2E8B57;
    }
    .paper-details {
        font-size: 16px !important;
        color: #333333;
    }
    .paper-card {
        background-color: #F0F8FF;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .paper-abstract {
        font-size: 14px !important;
        color: #555555;
        font-style: italic;
        margin-top: 10px;
    }
    .keyword {
        background-color: #E6E6FA;
        color: #4B0082;
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 12px !important;
        margin-right: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Published Papers</p>', unsafe_allow_html=True)

    # Journal Publications
    st.markdown('<p class="section-title">Journal Publications</p>', unsafe_allow_html=True)

    journal_papers = [

        {
            "title": "Optimizing Marketing Strategies: Integration of Al-Biruni Earth Radius ALGORITHM for Feature Selection and Pipeline Regression Model",
            "authors": "Mahmoud Elshabrawy Mohammed, Ahmed Mohamed Zaki, Marwa Eid, Khaled Gaber, Doaa Khafaga, Amel Alhussan",
            "journal": "IEEE Transactions on Artificial Intelligence",
            "year": "2024",
            "doi": "10.21608/jaiep.2024.354005",
            "abstract": "With the current business environment becoming increasingly ferocious, the effectiveness of digital marketing strategies is no longer a matter of debate as many organizations have realized the need to gain an edge over competition and improve the ROI with their marketing efforts. This study looks into the specifics of digital marketing effectiveness by, in the process, analyzing true indicators and key metrics. Demonstrating an understanding of the complexity of online marketing operations and the diversity of the variables involved, econometric techniques provide feature choice that affects campaign outcomes the most. At first, the variety of performance between different algorithms from feature selection gave the average error ranging from 0.38264 to 0.44194. However, following the optimization provides the tendency to see a decrease in mean errors and an improving performance. Afterward, the step of predictive modeling is implemented, employing diverse machine learning algorithms including ExtraTreesRegressor, GradientBoostingRegressor, SVR, and CatBoost to assess the effectiveness of foreshowing marketing outcomes. Before the optimization, the recommendations made by the predictive modeling are not too accurate and uniform for each algorithm. That being said, however, once the optimization is done, enhancement in prediction accuracy to the tune of substantial improvement is observed with metrics indicating the same as less MSE, RMSE, and R2. Contributing to a more thorough comprehension of the issue of selecting features and models for predicting as well as efficiency of digital marketing, the study also offers an understanding of the opportunities and obstacles that are present in the process of building digital marketing strategies. A thorough evaluation of top metrics and KPIs gives decision-makers data-driven tools to define their marketing activities, deliver tangible results, and stay relevant in the fast-paced digital environment of today.",
            "keywords": ["Digital marketing", "Feature Selection", "Predictive Modeling", "Metrics", "KPIs", "Optimization"]
        },
        {
            "title": "Optimizing Student Performance Prediction Using Binary Waterwheel Plant ALGORITHM for Feature Selection and Machine Learning",
            "authors": "Mahmoud Elshabrawy Mohammed, Basant Sameh, Ahmed Mohamed Zaki, Rizk Faris H., Karim Mohamed",
            "journal": "IEEE Transactions on Artificial Intelligence",
            "year": "2023",
            "doi": "10.54216/JAIM.070102",
            "abstract": "This paper deals with a pivotal part of educational data analytics, aiming to increase the accuracy and interpretability of student performance prediction models. The cornerstone of our method is the innovative application of binary waterwheel plant algorithm bWWPA in the feature selection. As we can see, an essential part of any model is the predicted values, which correctly define all the characteristics of this model. Practically, we begin with solid data pre-processing, which incorporates data cleaning and missing values, duplicate removal, and data transformation in order to get model input as optimally as possible. Preceding the application of bWWPA, we employ an ensemble of regression machine learning models. Set up a baseline for predictive capability, getting initial outcomes with an average Mean Squared Error (MSE) of 0.064. The following feature selection phase proceeds, showing the algorithm. Ability to recognize important elements and, as a result, improve model effectiveness and explain power. The comparative analyses after feature selection point to refined gains in the model, and the performance is reporting a lower MSE of 0.032 with the refined models. These findings, methodologically, add to student performance prediction. Accordingly, it emphasizes the decisive status of feature selection in improving models. The paper's significance extends to teachers, institutions, and researchers, giving insights into more precise and relevant student success-supporting interventions.",
            "keywords": ["feature selection", "student performance prediction", "Optimization", "educational data analysis", "regression models", "Waterwheel Plant Optimization ALGORITHM"]
        },
        {
            "title": "Seasonal Autoregressive Integrated Moving Average for Climate Change Time Series Forecasting",
            "authors": "Mahmoud Elshabrawy Mohammed , Basant Sameh ",
            "journal": "American Journal of Business and Operations Research",
            "year": "2022",
            "doi": "10.54216/AJBOR.080203",
            "abstract": "This study investigates the application of time series models, specifically ARIMA (Auto Regressive Integrated Moving Average) and SARIMAX (Seasonal Autoregressive Integrated Moving Average with eXogenous regressors), in the context of climate change. The ARIMA and SARIMAX models are mathematical methods that can be used to forecast future values of a time series related to climate change, taking into account trends and seasonality, as well as incorporating additional information through exogenous variables. The paper also delves into the mathematical foundations of the ARIMA and SARIMAX models, including the various operators used to eliminate trends, the use of lag polynomials to represent the autoregressive and moving average components of the model, and the incorporation of exogenous variables in the SARIMAX model. The study aims to provide a better understanding of the use of these models in analyzing and predicting the effects of climate change",
            "keywords": ["Forecasting ", "Time Series",
                         "ARIMA ", "SARIMAX ", "Climate Change"]
        },
        {
            "title": "Ocotillo Optimization ALGORITHM (OcOA): A Desert-Inspired Metaheuristic for Adaptive Optimization",
            "authors": "El-Sayed M. El-Kenawy, Rizk Faris H., Ahmed Mohamed Zaki, Mahmoud Elshabrawy Mohamed, Abdelhameed Ibrahim, Abdelaziz A. Abdelhamid, Nima Khodadadi, Ehab M. Almetwally, Marwa M. Eid",
            "journal": "Journal of Artificial Intelligence and Metaheuristics (JAIM)",
            "year": "2024",
            "doi": "10.54216/JAIM.080104",
            "abstract": "In this paper, we propose the Ocotillo Optimization Algorithm (OcOA), a novel desert-inspired metaheuristic designed to solve complex optimization problems. Inspired by the adaptive strategies of desert plants, OcOA aims to achieve a balance between exploration and exploitation in high-dimensional and multimodal search spaces. The algorithm dynamically adjusts its behavior based on feedback from prior iterations, optimizing both search breadth and solution refinement. To evaluate its effectiveness, OcOA was tested against several well-known algorithms on a range of benchmark functions, including unimodal and multimodal functions from the CEC 2005 suite such as Sphere, Rosenbrock, Ackley, and Rastrigin. The results demonstrate that OcOA outperforms competing approaches in terms of accuracy, convergence speed, and computational efficiency. Additionally, its adaptability was validated through feature selection tasks, highlighting its robustness in handling both continuous and discrete optimization challenges. This study positions OcOA as a competitive optimization tool for various real-world applications",
            "keywords": ["Ocotillo Optimization ALGORITHM", "metaheuristic", "exploration-exploitation balance", "complex optimization", "adaptive algorithm"]
        },
        {
            "title": "iHow Optimization ALGORITHM: A Human-Inspired Metaheuristic Approach for Complex Problem Solving and Feature Selection",
            "authors": "El-Sayed M. El-Kenawy, Rizk Faris H., Ahmed Mohamed Zaki, Mahmoud Elshabrawy Mohamed, Abdelhameed Ibrahim, Abdelaziz A. Abdelhamid, Nima Khodadadi, Ehab M. Almetwally, Marwa M. Eid",
            "journal": "Journal of Artificial Intelligence and Emerging Platforms (JAIEP)",
            "year": "2024",
            "doi": "10.21608/jaiep.2024.386694",
            "abstract": "In this paper, we propose the iHow Optimization Algorithm (iHowOA), a novel metaheuristic algorithm inspired by human-like cognitive processes such as learning, knowledge acquisition, and experience-based decision-making. The iHowOA aims to enhance the exploration-exploitation balance inherent to solving complex optimization problems by mimicking how humans gather data, learn, and improve over time. We tested the algorithm on standard benchmark functions, including those from the CEC 2005 suite, to evaluate its performance in terms of convergence, computational efficiency, and solution accuracy. Furthermore, the Binary iHowOA (biHowOA) was employed for feature selection tasks, and its performance was compared with other popular optimization algorithms. The results show that iHowOA achieves superior performance, consistently finding optimal solutions while maintaining computational efficiency. The biHowOA also demonstrated strong capability in feature selection, providing reduced feature sets with minimal classification error. Our experiments confirm that iHowOA offers an effective solution for both continuous optimization and feature selection challenges.",
            "keywords": ["iHow Optimization ALGORITHM", "metaheuristic", "human-inspired optimization", "feature selection", "complex problem solving", "machine learning"]
        },
        {
            "title": "NiOA: A Novel Metaheuristic Algorithm Modeled on the Stealth and Precision of Japanese Ninjas",
            "authors": "El-Sayed M. El-Kenawy, Rizk Faris H., Ahmed Mohamed Zaki, Mahmoud Elshabrawy Mohamed, Abdelhameed Ibrahim, Abdelaziz A. Abdelhamid, Nima Khodadadi, Ehab M. Almetwally, Marwa M. Eid",
            "journal": "Journal of Artificial Intelligence and Emerging Platforms (JAIEP)",
            "year": "2024",
            "doi": "10.21608/jaiep.2024.386693",
            "abstract": "This paper presents a new metaheuristic optimization algorithm called the Ninja Optimization Algorithm (NiOA) owing to its characteristics such as stealth, precision, and adaptability of the ninjas of Japan. NiOA is proposed to avoid high exploration and exploitation costs within such complex search spaces and to avoid the problem of getting trapped in local optima. The algorithm imitates ninja searching techniques because it has a scanning phase, adapted to search large areas to look for answers, while the more specific phase is used to refine the answers found. The performance of NiOA is compared with other benchmark optimization functions and some of the frequently used CEC 2005 benchmarks. These benchmarks are well suited to test unimodal and multimodal optimization problems of good quality. Experimental results prove that NiOA can significantly provide better optimization results regarding solution quality, convergence rate, and time complexity, suggesting that NiOA is a robust algorithm for solving high-dimensional large-scale optimization problems. Furthermore, it reveals that NiOA is applicable to solve different kinds of problem spaces, signifying that NiOA can be used in practice on scientific and engineering problems.",
            "keywords": ["Ninja Optimization ALGORITHM", "metaheuristic", "exploration and exploitation", "complex problem solving", "adaptive optimization"]
        },
        {
            "title": "Football Optimization ALGORITHM (FbOA): A Novel Metaheuristic Inspired by Team Strategy Dynamics",
            "authors": "El-Sayed M. El-Kenawy, Rizk Faris H., Ahmed Mohamed Zaki, Mahmoud Elshabrawy Mohamed, Abdelhameed Ibrahim, Abdelaziz A. Abdelhamid, Nima Khodadadi, Ehab M. Almetwally, Marwa M. Eid",
            "journal": "Journal of Artificial Intelligence and Emerging Platforms (JAIEP)",
            "year": "2024",
            "doi": "10.21608/jaiep.2024.384913",
            "abstract": "The Football Optimization Algorithm (FbOA) is introduced as a novel population-based metaheuristic optimization technique inspired by the dynamic strategies of a football team. Designed to address complex optimization problems characterized by high dimensionality, nonlinearity, and multiple local optima, FbOA draws on the strategic balance between exploration and exploitation observed in football gameplay. The algorithm mimics players' tactical positioning and movement, incorporating short passes, long passes, and positional adjustments to explore and exploit the solution space effectively. This study comprehensively evaluates the performance of FbOA using benchmark functions from the CEC 2005 test suite with 30-dimensional and 100-dimensional optimization problems. The results demonstrate that FbOA outperforms several state-of-the-art metaheuristic algorithms regarding convergence speed, accuracy, and robustness. The findings suggest that FbOA offers a promising alternative for solving various optimization challenges across multiple fields.",
            "keywords": ["Football Optimization ALGORITHM", "Metaheuristic Optimization", "Population-based Algorithm", "Complex Problem Solving", "Team Strategy Dynamics"]
        },
        {
            "title": "Machine Learning Approaches for Malaria Risk Prediction and Detection: Trends and Insights",
            "authors": "Ahmed Mohamed Zaki, Khaled Sh. Gaber, Faris H. Rizk, Mahmoud Elshabrawy Mohamed",
            "journal": "Malaria Outlook and Research (MOR)",
            "year": "2024",
            "doi": "10.54216/MOR.010105",
            "abstract": "The current review summarizes the latest trends in malaria literature, emphasizing transmission ecology, new diagnostics and treatment. It stresses the additional focus on the transmission, according to the spatiotemporal models and predictive analytics, which help identify periods and the locations with the most significant risk, noting that these processes should consider the environmental factors. The change in the diagnostic approach, especially the introduction of artificial intelligence techniques such as deep learning, has improved the rate and precision at which malaria parasites are diagnosed in resource-limited countries where time is of the essence. Furthermore, there have been significant advances in drug discovery due to machine learning applications that have made it quicker to find new antimalarial drugs in the face of drug resistance. Despite these developments, there are still problems such as drug resistance, socio-economic disparities, and the environment that are being altered and still require an integrated and transdisciplinary approach. Combining these determinants is indispensable for eliminating these challenges and further promoting global efforts to control malaria.",
            "keywords": ["Malaria", "Machine Learning", "Predictive Analytics", "Diagnostics", "Drug Discovery", "Transmission Ecology"]
        },
        {
            "title": "A Review on Waste Management Techniques for Sustainable Energy Production",
            "authors": "Mahmoud Elshabrawy Mohammed",
            "journal": "Malaria Outlook and Research (MOR)",
            "year": "2024",
            "doi": "10.54216/MOR.030205",
            "abstract": "Generating electricity from renewable and sustainable resources is one of the world's most urgent requirements because of the growing energy consumption and adverse effects of fossil fuels. Waste disposal provides a noble chance of. Currently, waste can produce energy to help conserve the environment and resources. That is why there is a need to introduce innovative WTE technologies, such as thermal, biological, and physicochemical processes, since global waste production is expected to rise by 70 percent by 2050. Such systems allow the energy to be reclaimed and reduce landfill and greenhouse gas incidents. Evolutionary approaches are most helpful in optimizing the system; they include genetic algorithms, particle swarms, and optimization neural networks. Integrating waste management, RE, and computational tools introduces potential approaches toward energy and waste. This work comprehensively reviewed integrated solutions for technical, operational, and social issues related to WTE implementation and provided innovative and economically reasonable ideas for future advancement.",
            "keywords": ["Waste Management", "Sustainable Energy", "Renewable Resources", "Waste-to-Energy", "Computational Optimization", "Environmental Conservation"]
        },
        {
            "title": "Interpretable Rainfall Forecasting Using SHAP-Enhanced Machine Learning: A Case Study on U.S. Urban Climate Data (2024-2025)",
            "authors": "Mahmoud Elshabrawy Mohammed, Khaled Sh. Gaber",
            "journal": "Journal of Artificial Intelligence and Metaheuristics (JAIM)",
            "year": "2024",
            "doi": "10.54216/JAIM.090203",
            "abstract": "Correct rainfall prediction is fundamental for developing resilient climates, guaranteeing sustainable farms and planned water distribution networks, and reducing possible disasters. Many meteorological elements affect rainfall patterns because rainfall shows nonlinear behavior and dependence across different timescales and diverse spatial areas. Multiple problematic features defeat conventional forecasting techniques because they produce insufficient accurate predictions of short-duration precipitation patterns. Because of rising climate variability, we require predictive frameworks built with data with strong performance abilities and human-understandable features. In this paper, we establish a machine learning that predicts daily rainfall in advance with a refined dataset consisting of detailed weather measurements spanning 20 United States metropolises from 2024 to 2025. The selected dataset contains six atmospheric factors: temperature, humidity, wind speed, and cloud cover with pressure and precipitation and a binary outcome to show rainfall prediction for the following day. Random Forest and Support Vector Machine (RBF) KNearest Neighbors (KNN), Logistic Regression, Naive Bayes, and Linear SVM formed the set of machine learning models that underwent training and evaluation. The SHAP method was integrated to improve prediction interpretation and trust through Shapley additive explanations value measures. SHAP values provided quantitative measurement and graphical visualization to explain the role of each input variable in making individual prediction outcomes. SHAP analysis of the model showcased precipitation and humidity as their most crucial features because they match the principles of meteorological theory and demonstrate the rational decision-making process of the model. The Random Forest approach scored the highest performance from all models, reaching perfect measurements for Precision = 100, Recall = 100 and F1-score = 100. The RBF SVM model alongside KNN showed strong performance since they delivered F1 scores of 0.97 and 0.94. The evaluation revealed that Logistic Regression, Linear SVM and Naive Bayes achieved satisfactory results, providing F1-score ratings between 0.76 and 0.77. The SHAP-based diagnostic results showed that Random Forest yielded exceptional classification results while simultaneously showing consistent weighting patterns between features across diverse locations. The integration of the Random Forest model with SHAP interpretation creates an effective solution for rainfall forecasting despite its high prediction capabilities. The model achieves complete prediction accuracy with precise explanation capabilities, generating trust for using it in actual deployment scenarios. According to the results, weather-sensitive sectors like agriculture, urban planning, and disaster response can leverage these transparent machine learning systems into their decision-making support pipelines. The approach described has the potential to become a model structure for conducting future predictive analyses in meteorology and environmental science.",
            "keywords": ["Rainfall Prediction", "SHAP", "Machine Learning", "Random Forest", "Climate Forecasting", "Interpretable AI"]
        },
    ]

    for paper in journal_papers:
        st.markdown(f"""
        <div class="paper-card">
            <p class="paper-title">{paper['title']}</p>
            <p class="paper-details"><strong>Authors:</strong> {paper['authors']}</p>
            <p class="paper-details"><strong>Journal:</strong> {paper['journal']}</p>
            <p class="paper-details"><strong>Year:</strong> {paper['year']}</p>
            <p class="paper-details"><strong>DOI:</strong> <a href="https://doi.org/{paper['doi']}" target="_blank">{paper['doi']}</a></p>
            <p class="paper-abstract"><strong>Abstract:</strong> {paper['abstract']}</p>
            <p class="paper-details"><strong>Keywords:</strong> {' '.join([f'<span class="keyword">{kw}</span>' for kw in paper['keywords']])}</p>
        </div>
        """, unsafe_allow_html=True)

    # Conference Proceedings
    st.markdown('<p class="section-title">Conference Proceedings</p>', unsafe_allow_html=True)

    conference_papers = [
        {
            "title": "Predictive Modeling of Portuguese Student Performance: Comparative Machine Learning Analysis",
            "authors": "Mahmoud elshabrawy Mohammed, El-Sayed M. El-kenawy, Marwa Eid, Basant Sameh, Ahmed Mohamed Zaki, Rizk Faris H.",
            "conference": "International Telecommunications Conference (ITC-Egypt)",
            "year": "2024",
            "doi": "10.1109/ITC-Egypt61547.2024.10620557",
            "abstract": "Such an analysis of different machine learning methods for predicting the achievement levels of students in Portuguese secondary education makes this essay. The research highlights the importance of accurate expectations of learners' results for education system administrations and respective policymakers. The current study makes use of the Student Performance in Portuguese Secondary education"
            " dataset and employs machine learning algorithms, namely MLPRegressor, XGBoost, DecisionTreeRegressor, CatBoost, and KNeighborsRe-gressor, to the corpus. Performance metrics such as mean squared error (MSE), root mean squared error (RMSE), mean absolute error (MAE), etc., are used to judge every model's performance. The conclusion that can be drawn from the data is that the MLPRegressor model leads among the competitors, having an MSE equivalent of 0.0103, which is superior to others. The findings of this study are of great significance for educational institutions and policymakers as they work to make appropriate contact with students' performance prediction.",
            "keywords": ["Education", "Machine learning", "Predictive models", "Data models"]
        },
        {
            "title": "Enhancing Student Performance Prediction with Greylag Goose Optimization ALGORITHM",
            "authors": "Mahmoud Elshabrawy Mohammed, Basant Sameh, El-Sayed M. El-kenawy, Marwa Eid, Ahmed Mohamed Zaki, Rizk Faris H.",
            "conference": "International Telecommunications Conference (ITC-Egypt)",
            "year": "2024",
            "doi": "10.1109/ITC-Egypt61547.2024.10620568",
            "abstract": "The current paper addresses the central role of hyperparameter optimization in improving the predictive power of the MLP Regressor for forecasting student performance in Portuguese secondary schools. The uniqueness of this research lies in its exploration of metaheuristic optimization algorithms, specifically highlighting GGO (Greylag Goose Optimization) for enhancement. The study utilized a dataset crucial for understanding and predicting student performance, with a special focus on its distinctive features. By comprehensively tuning the MLP Regressor, the paper demonstrates remarkable improvements in various performance measures, as evident in the enclosed tables. Specifically, the MSE values calculated for the MLP Regressor both before and after GGO optimization are compared. Without optimization, the MLP Regressor had an MSE of 0.0103. After GGO optimization, the MSE significantly improved to 0.0060, indicating enhanced accuracy with GGO in the model. These findings emphasize that hyperparameter optimization, particularly the GGO technique, is crucial for refining the MLP Regressor in predicting student performance. The paper not only delves into the technical aspects but also concludes by highlighting the broader consequences of these outcomes. The potential educational applications are substantial, as improved models can provide more accurate predictions, empowering educators and policymakers to make informed decisions in education. This paper establishes a foundation for future research directions, contributing to the pool of ideas for educational predictive modeling.",
            "keywords": ["Student Performance prediction", "Greylag Goose Optimization ALGORITHM", "MLP Regressor", "hyperparameter optimization", "education", "machine learning"]
        },
        {
            "title": "Forecasting of Monkeypox Cases Using Optimized SARIMAX Based Model",
            "authors": "Mahmoud Elshabrawy Mohammed, Basant Sameh, El-Sayed M. El-kenawy, Marwa Eid, Ahmed Mohamed Zaki, Rizk Faris H.",
            "conference": "3rd International Conference on Electronic Engineering (ICEEM)At: Menouf, Egypt",
            "year": "2023",
            "doi": "10.1109/ICEEM58740.2023.10319521",
            "abstract": "This study presents a dipper-throated-based ant colony optimization (DTACO) with the Seasonal Auto-Regressive Integrated Moving Average with eXogenous factor (SARIMAX) model (DTACO+SARIMAX) to forecast monkeypox cases. The work optimizes the SARIMAX model using grid search cross-validation and fine-tunes its hyperparameters using DTACO to improve prediction accuracy. The suggested model's consistency and accuracy are considerable compared to previous studies. Comparisons with state-of-the-art models validate the proposed model's predictions. DTACO+SARIMAX can be used to control disease and monitor monkeypox. Healthcare organizations and governments can better manage and track the pandemic's course by offering accurate predictions, reducing public panic, and enabling effective pandemic planning. The Analysis of Variance (ANOVA) and Wilcoxon signed-rank tests are conducted on the proposed DTACO-SARIMAX model and compared models.",
            "keywords": ["Analytical models", "Pandemics", "Monitoring", "Government", "Medical services", "Predictive models", "Reliability engineering"]
        },
        {
            "title": "Optimizing Wastewater Treatment Plant Operations: A Machine Learning Approach for Energy Consumption and Climate Dynamics Analysis",
            "authors": "Mahmoud Elshabrawy Mohammed, Marwa Eid, Abdelaziz A. Abdelhamid, Ali Takieldeen, El-Sayed M. El-kenawy",
            "conference": "8th IET SMART CITIES SYMPOSIUM - 2024, University of Bahrain",
            "year": "2024",
            "doi": "10.1049/IET-SCS.2024.12345",
            "abstract": "Treatment plant optimization plays an important role in the implementation of eco-problem solutions. This article is going to cover how machine learning algorithms can determine energy consumption, climate, and wastewater features of electricity at a wastewater treatment plant in eastern Melbourne from 2014 to 2019. This study uses data obtained from the Melbourne Water and Airport weather station, which are freely available to carry out MLPRegressor, SVM, Linear Regression, Decision Tree Regression, random forest regression, and Nearest Neighbor. Through customary measures like MSE, RMSE, EVS, and others, the best model is adequately identified, which is the Random Forest Regressor model, which has 0.889285. (Lowest MSE) With these results, the plant treatment optimization processes, such as sampling for environmental analysis and the control of energy consumption, have improved.",
            "keywords": ["Wastewater Treatment", "Machine Learning", "Energy Consumption", "Climate Dynamics", "Random Forest Regression", "Optimization"]
        },
    ]

    for paper in conference_papers:
        st.markdown(f"""
        <div class="paper-card">
            <p class="paper-title">{paper['title']}</p>
            <p class="paper-details"><strong>Authors:</strong> {paper['authors']}</p>
            <p class="paper-details"><strong>Conference:</strong> {paper['conference']}</p>
            <p class="paper-details"><strong>Year:</strong> {paper['year']}</p>
            <p class="paper-details"><strong>DOI:</strong> <a href="https://doi.org/{paper['doi']}" target="_blank">{paper['doi']}</a></p>
            <p class="paper-abstract"><strong>Abstract:</strong> {paper['abstract']}</p>
            <p class="paper-details"><strong>Keywords:</strong> {' '.join([f'<span class="keyword">{kw}</span>' for kw in paper['keywords']])}</p>
        </div>
        """, unsafe_allow_html=True)

    # Call to action
    st.markdown("""
    <div style="text-align: center; margin-top: 50px;">
        <p class="paper-details">Interested in collaborating on research or discussing my publications?</p>
        <a href="mailto:mahmoudelshabrawy662001@gmail.com" style="background-color: #1E90FF; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">Contact Me</a>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    papers_page()