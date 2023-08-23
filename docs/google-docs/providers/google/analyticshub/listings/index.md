---
title: listings
hide_title: false
hide_table_of_contents: false
keywords:
  - listings
  - analyticshub
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>listings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.analyticshub.listings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the listing. e.g. `projects/myproject/locations/US/dataExchanges/123/listings/456` |
| `description` | `string` | Optional. Short description of the listing. The description must not contain Unicode non-characters and C0 and C1 control codes except tabs (HT), new lines (LF), carriage returns (CR), and page breaks (FF). Default value is an empty string. Max length: 2000 bytes. |
| `icon` | `string` | Optional. Base64 encoded image representing the listing. Max Size: 3.0MiB Expected image dimensions are 512x512 pixels, however the API only performs validation on size of the encoded data. Note: For byte fields, the contents of the field are base64-encoded (which increases the size of the data by 33-36%) when using JSON on the wire. |
| `state` | `string` | Output only. Current state of the listing. |
| `requestAccess` | `string` | Optional. Email or URL of the request access of the listing. Subscribers can use this reference to request access. Max Length: 1000 bytes. |
| `bigqueryDataset` | `object` | A reference to a shared dataset. It is an existing BigQuery dataset with a collection of objects such as tables and views that you want to share with subscribers. When subscriber's subscribe to a listing, Analytics Hub creates a linked dataset in the subscriber's project. A Linked dataset is an opaque, read-only BigQuery dataset that serves as a _symbolic link_ to a shared dataset. |
| `dataProvider` | `object` | Contains details of the data provider. |
| `documentation` | `string` | Optional. Documentation describing the listing. |
| `categories` | `array` | Optional. Categories of the listing. Up to two categories are allowed. |
| `publisher` | `object` | Contains details of the listing publisher. |
| `displayName` | `string` | Required. Human-readable display name of the listing. The display name must contain only Unicode letters, numbers (0-9), underscores (_), dashes (-), spaces ( ), ampersands (&) and can't start or end with spaces. Default value is an empty string. Max length: 63 bytes. |
| `restrictedExportConfig` | `object` | Restricted export config, used to configure restricted export on linked dataset. |
| `primaryContact` | `string` | Optional. Email or URL of the primary point of contact of the listing. Max Length: 1000 bytes. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_data_exchanges_listings_get` | `SELECT` | `dataExchangesId, listingsId, locationsId, projectsId` | Gets the details of a listing. |
| `projects_locations_data_exchanges_listings_list` | `SELECT` | `dataExchangesId, locationsId, projectsId` | Lists all listings in a given project and location. |
| `projects_locations_data_exchanges_listings_create` | `INSERT` | `dataExchangesId, locationsId, projectsId` | Creates a new listing. |
| `projects_locations_data_exchanges_listings_delete` | `DELETE` | `dataExchangesId, listingsId, locationsId, projectsId` | Deletes a listing. |
| `_projects_locations_data_exchanges_listings_list` | `EXEC` | `dataExchangesId, locationsId, projectsId` | Lists all listings in a given project and location. |
| `projects_locations_data_exchanges_listings_patch` | `EXEC` | `dataExchangesId, listingsId, locationsId, projectsId` | Updates an existing listing. |
| `projects_locations_data_exchanges_listings_subscribe` | `EXEC` | `dataExchangesId, listingsId, locationsId, projectsId` | Subscribes to a listing. Currently, with Analytics Hub, you can create listings that reference only BigQuery datasets. Upon subscription to a listing for a BigQuery dataset, Analytics Hub creates a linked dataset in the subscriber's project. |
