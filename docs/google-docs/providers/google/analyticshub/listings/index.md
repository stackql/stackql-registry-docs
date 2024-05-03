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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>listings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.analyticshub.listings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the listing. e.g. `projects/myproject/locations/US/dataExchanges/123/listings/456` |
| <CopyableCode code="description" /> | `string` | Optional. Short description of the listing. The description must not contain Unicode non-characters and C0 and C1 control codes except tabs (HT), new lines (LF), carriage returns (CR), and page breaks (FF). Default value is an empty string. Max length: 2000 bytes. |
| <CopyableCode code="bigqueryDataset" /> | `object` | A reference to a shared dataset. It is an existing BigQuery dataset with a collection of objects such as tables and views that you want to share with subscribers. When subscriber's subscribe to a listing, Analytics Hub creates a linked dataset in the subscriber's project. A Linked dataset is an opaque, read-only BigQuery dataset that serves as a _symbolic link_ to a shared dataset. |
| <CopyableCode code="categories" /> | `array` | Optional. Categories of the listing. Up to two categories are allowed. |
| <CopyableCode code="dataProvider" /> | `object` | Contains details of the data provider. |
| <CopyableCode code="displayName" /> | `string` | Required. Human-readable display name of the listing. The display name must contain only Unicode letters, numbers (0-9), underscores (_), dashes (-), spaces ( ), ampersands (&) and can't start or end with spaces. Default value is an empty string. Max length: 63 bytes. |
| <CopyableCode code="documentation" /> | `string` | Optional. Documentation describing the listing. |
| <CopyableCode code="icon" /> | `string` | Optional. Base64 encoded image representing the listing. Max Size: 3.0MiB Expected image dimensions are 512x512 pixels, however the API only performs validation on size of the encoded data. Note: For byte fields, the contents of the field are base64-encoded (which increases the size of the data by 33-36%) when using JSON on the wire. |
| <CopyableCode code="primaryContact" /> | `string` | Optional. Email or URL of the primary point of contact of the listing. Max Length: 1000 bytes. |
| <CopyableCode code="publisher" /> | `object` | Contains details of the listing publisher. |
| <CopyableCode code="requestAccess" /> | `string` | Optional. Email or URL of the request access of the listing. Subscribers can use this reference to request access. Max Length: 1000 bytes. |
| <CopyableCode code="restrictedExportConfig" /> | `object` | Restricted export config, used to configure restricted export on linked dataset. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the listing. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_data_exchanges_listings_get" /> | `SELECT` | <CopyableCode code="dataExchangesId, listingsId, locationsId, projectsId" /> | Gets the details of a listing. |
| <CopyableCode code="projects_locations_data_exchanges_listings_list" /> | `SELECT` | <CopyableCode code="dataExchangesId, locationsId, projectsId" /> | Lists all listings in a given project and location. |
| <CopyableCode code="projects_locations_data_exchanges_listings_create" /> | `INSERT` | <CopyableCode code="dataExchangesId, locationsId, projectsId" /> | Creates a new listing. |
| <CopyableCode code="projects_locations_data_exchanges_listings_delete" /> | `DELETE` | <CopyableCode code="dataExchangesId, listingsId, locationsId, projectsId" /> | Deletes a listing. |
| <CopyableCode code="_projects_locations_data_exchanges_listings_list" /> | `EXEC` | <CopyableCode code="dataExchangesId, locationsId, projectsId" /> | Lists all listings in a given project and location. |
| <CopyableCode code="projects_locations_data_exchanges_listings_patch" /> | `EXEC` | <CopyableCode code="dataExchangesId, listingsId, locationsId, projectsId" /> | Updates an existing listing. |
| <CopyableCode code="projects_locations_data_exchanges_listings_subscribe" /> | `EXEC` | <CopyableCode code="dataExchangesId, listingsId, locationsId, projectsId" /> | Subscribes to a listing. Currently, with Analytics Hub, you can create listings that reference only BigQuery datasets. Upon subscription to a listing for a BigQuery dataset, Analytics Hub creates a linked dataset in the subscriber's project. |
