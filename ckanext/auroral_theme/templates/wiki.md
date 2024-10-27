
# AURORAL Data Catalogue 

---

## Table of Contents

1. [What is the AURORAL Data Catalogue?](#what-is-the-auroral-data-catalogue)
2. [Prerequisites](#prerequisites)
3. [Describing your dataset](#describing-your-dataset)
4. [How to Register a Dataset in the Node](#how-to-register-a-dataset-in-the-node)
5. [How to display it in the AURORAL Data Catalogue](#how-to-display-it-in-the-auroral-data-catalogue)
6. [Common Issues and Troubleshooting](#common-issues-and-troubleshooting)
7. [FAQ](#faq)
8. [Contact](#contact)

---

## What is the AURORAL Data Catalogue?

The AURORAL Data Catalogue (http://auroraldatacatalogue.eu) is an open data portal that provides a catalog of data resources from the entities participating in the AURORAL project. It serves as a key tool for showcasing and making accessible the datasets created within the project.

Unlike traditional data storage systems, the AURORAL Data Catalogue does not store data directly. Instead, it offers a centralized directory where resources are listed and linked to the locations (URIs) where the actual datasets are hosted. This approach ensures that data remains decentralized and under the control of the entities that produce it, promoting privacy and security.

The service is fully automated and works through the AURORAL middleware, which discovers and registers datasets from the AURORAL nodes in real time. By leveraging this middleware, the Data Catalogue provides an up-to-date view of available datasets, automatically reflecting any changes in the underlying data nodes, such as when a dataset is added or removed.

This cataloging service supports a wide range of domains, including mobility, energy, health, and tourism, among others, allowing organizations to share and discover data resources easily. Through this platform, users can search for and filter datasets based on various criteria, making it a powerful tool for fostering collaboration and innovation across different sectors.

![enter image description here](https://i.postimg.cc/BZLQcc2w/landingpage.png)

---

## Prerequisites

Before using the AURORAL Data Catalogue service, ensure you meet the following requirements:

- **AURORAL Platform Account**: You must have an account on the [AURORAL Platform](https://auroral.bavenir.eu/). This is necessary for accessing the AURORAL middleware and connecting through the node.
  
- **AURORAL Node Deployment**: You need to have a deployed AURORAL Node in your infrastructure. The node will serve as the interface to register and expose your datasets through the AURORAL middleware. You can install your node following the instructions in the [AURORAL Documentation](https://auroral.docs.bavenir.eu/getting_started/install_node/)

- **Community Membership**: Your node must be part of the Data Catalogue community within the AURORAL Neighbourhood Manager. This membership is required to facilitate the exchange of metadata between the service and the participating nodes.

- **Web of Things (WoT) Description**: Datasets must be described using the Web of Things (WoT) format. This ensures that the metadata is standardized and compatible with the AURORAL ecosystem.

---
## Describing your dataset
The datasets in the AURORAL platform are described according to the **Web of Things (WoT) Dictionary**, which allows for standardized metadata representation. You can easily register your dataset by using the following template and replacing the placeholder values with your actual dataset information:

```json
{
  "@context": [
    "https://www.w3.org/2019/wot/td/v1",
    {
      "adp": "https://auroral.iot.linkeddata.es/def/adapters#",
      "om": "http://www.ontology-of-units-of-measure.org/resource/om-2/",
      "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
      "schema": "https://schema.org/"
    }
  ],
  "security": [
    "nosec_sc"
  ],
  "securityDefinitions": {
    "nosec_sc": {
      "scheme": "nosec"
    }
  },
  "title": "The title for your dataset",
  "@type": "adp:Dataset",
  "domain": "Your domaain",
  "provider":"The name of your company/institution",
  "description": "A description of your dataset",
  "url": "The url for accessing your data"
} 
```

Replace the following fields: 
- `"title"`: Provide the title of your dataset. 
- `"domain"`: Indicate the domain. Availabe domains are mobility, energy, health, farming, tourism and other. 
- `"provider"`: Your company or institution's name. 
- `"description"`: A detailed description of the dataset. 
- `"url"`: The URL where the dataset can be accessed. 

Once this information is set, you are ready to use the AURORAL API to register your dataset.


## How to Register a Dataset in the Node

1. **Access the Node**: - Open a web browser and navigate to the node using its IP address and port. The format is `http://<node-ip>:<port>`. - Example: `http://192.168.1.10:81` or `http://localhost:81`. 

2. **Choose an Interface**: - You have two options for interacting with the node: 

- **API**: You can use the AURORAL Open API to register datasets 
- **Node UI**: You can also use the Node's web-based User Interface (UI) to do it


	2.1. **Using the AURORAL Node UI**: 
	Access the NODE UI by adding `/ui` at the end of your node url (example `http://localhost:81/ui`) and then go to the "My Node" section in the left-side menu. This section will allow you to magane the items available in your node, including datasets.

	There are two ways to register a new dataset though the UI:

	- Click on the **+ New item** button located on the right side of the page, as shown in the image above: You will be presented with two options: 
	-- **Use Editor**: This allows you to manually input the metadata for the dataset through an editor. 
	-- **Upload TD**: This allows you to upload a Thing Description (TD) file, which follows the Web of Things (WoT) format.

![enter image description here](https://i.postimg.cc/yNSCmyby/IU-options.png)

In this case, given that the description of data template is provided, go to Upload TD and copy-paste the thing description of your data in the < Code > tab:
		
![enter image description here](https://i.postimg.cc/BbprSYj4/TDUI.png)


Then, click on + Create Item and your dataset description will be created.

After successfully registering the description of your datasets, it will appear in the list of datasets with a **NEW** label, as shown in the image below:


![enter image description here](https://i.postimg.cc/FK0HxvfR/registereditems.png)

By clicking on the item name, you will be able remove or edit the dataset description:

![enter image description here](https://i.postimg.cc/h40W1jp6/removeedit.png)


2.1.**Using the API**:
	
**NOTE:** when using the API to register a dataset, it is necessary to make a slight modification to the Thing 	Description (TD). Below, we include the modified TD description that should be used for registration.
```json	
{
"td": {
  "@context": [
    "https://www.w3.org/2019/wot/td/v1",
    {
      "adp": "https://auroral.iot.linkeddata.es/def/adapters#",
      "om": "http://www.ontology-of-units-of-measure.org/resource/om-2/",
      "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
      "schema": "https://schema.org/"
    }
  ],
  "security": [
    "nosec_sc"
  ],
  "securityDefinitions": {
    "nosec_sc": {
      "scheme": "nosec"
    }
  },
  "title": "The title for your dataset",
  "@type": "adp:Dataset",
  "domain": "Your doain",
  "provider":"The name of your company/institution",
  "description": "A description of your dataset",
  "url": "The url for accesing your data"
   },
    "avatar": "nostrud sunt"
}
 ```

Go to `/api/registation` and copy the WoT description of your data. 

![enter image description here](https://i.postimg.cc/zXds4Qmk/registering1.png)
 
Then click execute and you will receive the following response, with a 201 code indicating that it was sucesfully registered:
	
![enter image description here](https://i.postimg.cc/9QR3GB4F/response1.png)

For for detailed instructions on how to submit/update or delete metadata in the Web of Things (WoT) format please refer to the [AURORAL Open API documentation](https://auroralh2020.github.io/auroral-node-agent/) . 


## How to display them in the AURORAL Data Catalogue


Once you have registered your datasets, follow these steps to display them in the AURORAL Data Catalogue:

1. **Access the AURORAL Platform**:
   - Log in to the [AURORAL Platform](https://auroral.bavenir.eu/).
   
2. **Join the Data Catalogue Community**:
**Note**: This step only needs to be done the first time you use a node to register datasets. If you use a different node in the future, you'll need to repeat this process for that node.

   - Navigate to the **Communities** section from the left-hand menu.
   - Locate the **Data Catalogue Community** and access it. This community enables your node to interact with the AURORAL Data Catalogue.
				
		![enter image description here](https://i.postimg.cc/Ss75dT7C/communities.png)

   - To join the community, click on  **Update My Nodes** inside the Data Catalogue Community. You can do it just by pressing the red arrow on the node you are registering the dataset unti a green check mark appears.  
	
		
	
		![enter image description here](https://i.postimg.cc/c1h28zJN/enable.png)

		This way, you enable the node where you registered your datasets to share the metadata with the community. This step ensures that the node's datasets are synchronized with the AURORAL platform. To remove a Node from the community, do the opposite.
	   - Remember that you only need to update your node again if you use a different node in the future.

3. **Enable Dataset for Public Access**:
To be able to share data with the community you also need to enable the item (dataset) and change visibility level. For that:
   - Go to the **Items** section, where you will find the datasets registered through your node.
   
	   ![enter image description here](https://i.postimg.cc/HkqhgD6b/enable-item.png)
   
   - Click on the dataset you wish to display.
   - Within the item view, click on **Enable Device** to make the dataset active.
   
	   ![enter image description here](https://i.postimg.cc/L58yTHsF/enable2.png)
   
   - In the **Visibility Level** settings, choose **Public with data under request**. This option allows users to discover the dataset in the catalogue and request access to the data.

		![enter image description here](https://i.postimg.cc/hGRpY8Gr/visibility.png)

**Now you dataset registration process is over!**

6. **Wait for Dataset to Appear**:
   - After enabling the dataset and setting the visibility, wait a few seconds. The dataset will automatically appear in the AURORAL Data Catalogue for other users to discover and request access.

Once these steps are completed, your dataset will be available to the public through the AURORAL Data Catalogue.


## Common Issues and Troubleshooting

**What should I do if my dataset doesn’t appear in the catalogue?**
   - Ensure that you have:
     - Enabled the dataset item by clicking **Enable Device**.
     - Set the visibility level to **Public with data under request**.
     - Waited a few seconds for the catalogue to refresh.
   - If the issue persists, verify that your node is properly connected to the **Data Catalogue Community** and that there are no network issues. 



## FAQ

### 1. **How can I edit the photo and description of my organization in the AURORAL Data Catalogue?**
   - To edit the profile photo and description of your organization, you need to fill out a form with the desired information.
[Link to the form](https://docs.google.com/forms/d/e/1FAIpQLSdqbQialLEPqtUokHXuNoDL4DXFgb52Fd1Ag0xUnfQLUsZ1Mg/viewform?usp=sf_link)

		Include the new description text and the profile image you want to use, then submit it to the AURORAL support team. 	The data catalogue will be upadted with your changes.

### 2. **Do I need to update my node every time I register a new dataset?**
   - **No**, you only need to update your node the first time you use it to register datasets. If you decide to use a different node in the future, you will need to update that new node. However, for the same node, you don't need to repeat this process for subsequent dataset registrations.

### 3. **How long does it take for a dataset to appear in the AURORAL Data Catalogue?**
   - After enabling the dataset and setting its visibility to "Public with data under request", it should appear in the catalogue within a minute.

### 4. **Can I register multiple datasets through the same node?**
   - **Yes**, you can register multiple datasets either through the **Node UI** or by uploading multiple **Thing Descriptions (TD)** via the API. Just make sure that each dataset has its unique metadata and is correctly formatted.

### 5. **Can I delete a dataset?**
   - **Yes**, if a dataset is deleted from the node where it was registered, it will automatically be removed from the AURORAL Data Catalogue as well. This ensures that the catalogue stays up to date with the data available in the nodes. However, please note that the removal process usually takes longer than the registration process to be reflected in the catalogue.

### 6. **Can I make a dataset private after making it public?**
   - **Yes**, you can change the visibility setting from "Public" to "Private" at any time. Simply access the dataset in the **Items** section, and adjust the visibility level. Once set to private, your dataset will no longer appear in the public catalogue.

### 7. **How do I edit an already registered dataset?**
   - You can edit the metadata of a dataset through the **Node UI**. Access the dataset via the **Items** section, make the necessary changes, and submit the updated information. The changes will reflect in the AURORAL Data Catalogue shortly after.


## Contact

**If you encounter any issues or require further assistance, please do not hesitate to contact Oihane Gómez at oihane.gomezc@deusto.es.**