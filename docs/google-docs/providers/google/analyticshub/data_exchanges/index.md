---
title: data_exchanges
hide_title: false
hide_table_of_contents: false
keywords:
  - data_exchanges
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
<tr><td><b>Name</b></td><td><code>data_exchanges</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.analyticshub.data_exchanges" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the data exchange. e.g. `projects/myproject/locations/US/dataExchanges/123`. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the data exchange. The description must not contain Unicode non-characters as well as C0 and C1 control codes except tabs (HT), new lines (LF), carriage returns (CR), and page breaks (FF). Default value is an empty string. Max length: 2000 bytes. |
| <CopyableCode code="displayName" /> | `string` | Required. Human-readable display name of the data exchange. The display name must contain only Unicode letters, numbers (0-9), underscores (_), dashes (-), spaces ( ), ampersands (&) and must not start or end with spaces. Default value is an empty string. Max length: 63 bytes. |
| <CopyableCode code="documentation" /> | `string` | Optional. Documentation describing the data exchange. |
| <CopyableCode code="icon" /> | `string` | Optional. Base64 encoded image representing the data exchange. Max Size: 3.0MiB Expected image dimensions are 512x512 pixels, however the API only performs validation on size of the encoded data. Note: For byte fields, the content of the fields are base64-encoded (which increases the size of the data by 33-36%) when using JSON on the wire. |
| <CopyableCode code="listingCount" /> | `integer` | Output only. Number of listings contained in the data exchange. |
| <CopyableCode code="primaryContact" /> | `string` | Optional. Email or URL of the primary point of contact of the data exchange. Max Length: 1000 bytes. |
| <CopyableCode code="sharingEnvironmentConfig" /> | `object` | Sharing environment is a behavior model for sharing data within a data exchange. This option is configurable for a data exchange. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_data_exchanges_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists all data exchanges from projects in a given organization and location. |
| <CopyableCode code="projects_locations_data_exchanges_get" /> | `SELECT` | <CopyableCode code="dataExchangesId, locationsId, projectsId" /> | Gets the details of a data exchange. |
| <CopyableCode code="projects_locations_data_exchanges_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all data exchanges in a given project and location. |
| <CopyableCode code="projects_locations_data_exchanges_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new data exchange. |
| <CopyableCode code="projects_locations_data_exchanges_delete" /> | `DELETE` | <CopyableCode code="dataExchangesId, locationsId, projectsId" /> | Deletes an existing data exchange. |
| <CopyableCode code="_organizations_locations_data_exchanges_list" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId" /> | Lists all data exchanges from projects in a given organization and location. |
| <CopyableCode code="_projects_locations_data_exchanges_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists all data exchanges in a given project and location. |
| <CopyableCode code="projects_locations_data_exchanges_patch" /> | `EXEC` | <CopyableCode code="dataExchangesId, locationsId, projectsId" /> | Updates an existing data exchange. |
| <CopyableCode code="projects_locations_data_exchanges_subscribe" /> | `EXEC` | <CopyableCode code="dataExchangesId, locationsId, projectsId" /> | Creates a Subscription to a Data Exchange. This is a long-running operation as it will create one or more linked datasets. |
