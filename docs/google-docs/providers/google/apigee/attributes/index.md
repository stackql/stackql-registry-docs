---
title: attributes
hide_title: false
hide_table_of_contents: false
keywords:
  - attributes
  - apigee
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
<tr><td><b>Name</b></td><td><code>attributes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="apigee.attributes" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_apiproducts_attributes_get" /> | `SELECT` | <CopyableCode code="apiproductsId, attributesId, organizationsId" /> | Gets the value of an API product attribute. |
| <CopyableCode code="organizations_apiproducts_attributes_list" /> | `SELECT` | <CopyableCode code="apiproductsId, organizationsId" /> | Lists all API product attributes. |
| <CopyableCode code="organizations_developers_apps_attributes_get" /> | `SELECT` | <CopyableCode code="appsId, attributesId, developersId, organizationsId" /> | Returns a developer app attribute. |
| <CopyableCode code="organizations_developers_apps_attributes_list" /> | `SELECT` | <CopyableCode code="appsId, developersId, organizationsId" /> | Returns a list of all developer app attributes. |
| <CopyableCode code="organizations_developers_attributes_get" /> | `SELECT` | <CopyableCode code="attributesId, developersId, organizationsId" /> | Returns the value of the specified developer attribute. |
| <CopyableCode code="organizations_developers_attributes_list" /> | `SELECT` | <CopyableCode code="developersId, organizationsId" /> | Returns a list of all developer attributes. |
| <CopyableCode code="organizations_apiproducts_attributes_delete" /> | `DELETE` | <CopyableCode code="apiproductsId, attributesId, organizationsId" /> | Deletes an API product attribute. |
| <CopyableCode code="organizations_developers_apps_attributes_delete" /> | `DELETE` | <CopyableCode code="appsId, attributesId, developersId, organizationsId" /> | Deletes a developer app attribute. |
| <CopyableCode code="organizations_developers_attributes_delete" /> | `DELETE` | <CopyableCode code="attributesId, developersId, organizationsId" /> | Deletes a developer attribute. |
