---
title: service_classes
hide_title: false
hide_table_of_contents: false
keywords:
  - service_classes
  - networkconnectivity
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
<tr><td><b>Name</b></td><td><code>service_classes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkconnectivity.service_classes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The name of a ServiceClass resource. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/serviceClasses/&#123;service_class&#125; See: https://google.aip.dev/122#fields-representing-resource-names |
| <CopyableCode code="description" /> | `string` | A description of this resource. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the ServiceClass was created. |
| <CopyableCode code="etag" /> | `string` | Optional. The etag is computed by the server, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | User-defined labels. |
| <CopyableCode code="serviceClass" /> | `string` | Output only. The generated service class name. Use this name to refer to the Service class in Service Connection Maps and Service Connection Policies. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the ServiceClass was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, serviceClassesId" /> | Gets details of a single ServiceClass. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists ServiceClasses in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, serviceClassesId" /> | Deletes a single ServiceClass. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists ServiceClasses in a given project and location. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, serviceClassesId" /> | Updates the parameters of a single ServiceClass. |
