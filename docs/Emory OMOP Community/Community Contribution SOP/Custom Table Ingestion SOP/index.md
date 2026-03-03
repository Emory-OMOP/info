# Purpose of the Document

Collaboration across Emory on pushing data from a source database to target OMOP location in a reliable pipeline is highly recommended given the significant burden that comes with a) identifying useful data locations from source (Epic/CDW), b) understanding how that data must be reliably cleaned for research readiness, and c) understanding how that data should best fit into the OMOP model. The Enterprise OMOP group has attempted to identify the most common tables and columns from Epic that will need to be in the CDM for this product release stage (see top of document), but we are certain we've missed data that is critical to end user needs. For that reason, we're attempting to distribute the workload to some degree, while simultaneously being able to quickly implement features provided by users.

## When to Use this SOP

If you know the data exists in the source system (either Epic or CDW), that is the critical first step! If you know more than that, then we'll be well on our way to implementing the changes you suggest. 

## When not to use this SOP

If you don't know if the data exists, but are convinced it SHOULD exist somewhere and don't know where to start looking, these are the most difficult to track down, and the most challenging for the Enterprise OMOP team to address. Before approaching the next steps in the SOP process, you or a member of your team may wish to review critical data elements in an attempt to find a marker of where that type of data is located in the source system, and keep notes so that you are prepared to share those markers with the enterprise OMOP team (more on that later). You will want to begin to approach the task at the level you are most familiar with the data. For example, if you are a clinician working in hyperspace, finding the data in Epic, and getting us the INI number for the particular data element you are looking for will make collaborative work FAR easier (holding shift on your keyboard, and then clicking on an item with the left mouse button will give you critical details about the data element)! Alternatively, being able to create a SlicerDicer dashboard with the data you are interested in is another great first step! In turn, if you are an analyst, using slicer dicer, or finding the element in Clarity Data Dictionary or Reporting Workbench, will similarly be your first approach.

You are always welcome to reach out to us, at any time, but unfortunately our time is quite limited. This causes us to focus on the most critical data elements first that will have the most impact on the widest segment of the Emory research community. If you are not sure if your data element is critical, please reach out to us, and we can help you determine if it is currently on, or can be added to, our Product Roadmap.

### Where to go if you're not yet ready for the SOP

We encourage you to use the tools and the communities that are readily at your disposal at Emory to help with finding the tables and columns you are looking for. The following resources are available to you at the time of this writing.

**Community Resources**
- Epic Suite of Resources (not limited to the following)
    - Cogito
    - Galaxy
    - Clarity Data Dictionary
    - Epic Userweb
    - Hyperspace
    - [Epic Clarity Data Dictionary](https://userweb.epic.com/Documentation/ClarityDataDictionary/ClarityDataDictionary.html)
    - [Epic Userweb](https://userweb.epic.com/)
- OHDSI and Emory OMOP community (also see Ohdsi Conventions documentation on this site)
    - [OHDSI Forums](https://forums.ohdsi.org/)
    - OHDSI Workgroups (data type and disease specific)
        - Teams spaces and Workgroup calls are a great place for newcomers to ask questions
    - [General channel](https://teams.microsoft.com/l/channel/19%3AtGpixXm22J177ODEAB2sQ_OHDEG5QzQmR7tOZLGmnEE1%40thread.tacv2/General?groupId=1daa5866-d1b0-4677-8190-37516c91ca06&tenantId=e004fb9c-b0a4-424f-bcd0-322606d5df38) in the enterprise OMOP MS Teams space.
    - Head to Jira, and filter tickets by the "Feature" epic (grouper in Jira) to see what other people are working on, and what is in the pipeline.

## Where to go when you're ready to use this SOP

1) complete the brief OMOP User Source-Target Knowledge self-assessment form (🚧 under construction as of release date 🚧).
2) complete the OMOP Source to Target Data Mapping Template (🚧 under construction as of release date 🚧)
    - you can provide as much or as little detail as you like, but the more detail you provide, the easier it will be for us to implement your request.
3) attend the next Enterprise OMOP Community Meeting to discuss the request with the team and with other users
    - this is a great time to ask questions about the data, and to get feedback from the community on your request
    - please note that the team will try and review your request before the meeting, but the more leed time you give us, the better we can prepare for the meeting
4) by completing 1 and 2, you will have created a Jira ticket for your request. The team will review the request and get back to you with any questions or comments if you do not otherwise reach out to the team in some manner (such as step 3, above).