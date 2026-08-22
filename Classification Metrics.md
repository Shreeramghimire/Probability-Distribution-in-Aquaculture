**Classification metrics** are quantitative measures used to evaluate the performance of machine learning models that predict categorical outcomes. They answer critical questions like: *"How accurate is my model?"*, *"What types of mistakes does it make?"*, and *"Can I trust its predictions in production?"*

While accuracy is the most intuitive metric, it often tells an incomplete story—especially when dealing with **imbalanced datasets** or when **different types of errors have vastly different consequences**.

**The Core Principle:** *No single metric captures everything. Understanding the trade-offs is the key to building trustworthy models.*

**Why Classification Metrics Matter in Aquaculture:**

Aquaculture, particularly **Atlantic salmon farming**, generates massive amounts of data from:
- **Sensors** (oxygen, temperature, pH, salinity)
- **Video feeds** (fish counting, behavior analysis)
- **Health records** (disease outbreaks, parasite loads)
- **Feeding systems** (automated feeders, consumption rates)

Machine learning models are increasingly deployed to classify:

| Application | Classification Task | Business Impact |
|:---|:---|:---|
|  **Disease Detection** | Identify if a fish has *ISA virus* or *PD* (Positive/Negative) | Early detection saves millions in stock loss |
|  **Sea Lice Monitoring** | Classify lice load as *Low/Medium/High* | Determines treatment timing and costs |
|  **Feeding Optimization** | Predict if fish are *Hungry/Neutral/Full* | Reduces feed waste (30% of operational cost) |
|  **Mortality Prediction** | Flag *At-Risk* fish pens | Enables proactive intervention |
|  **Harvest Quality** | Grade salmon as *Premium/Standard/Reject* | Maximizes export revenue |
|  **Sex Classification** | Classify *Male/Female* using genetic markers | Optimizes breeding programs |

**The stakes are high:**
- A **False Negative** in disease detection means a sick fish spreads infection, potentially wiping out an entire pen.
- A **False Positive** in feeding means wasting expensive feed and polluting the water.
- A **False Negative** in mortality prediction delays intervention, increasing mortality rates.

Choosing the right metric directly impacts **profitability, sustainability, and animal welfare**.


