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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_classes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkconnectivity.service_classes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The name of a ServiceClass resource. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/serviceClasses/&#123;service_class&#125; See: https://google.aip.dev/122#fields-representing-resource-names |
| `description` | `string` | A description of this resource. |
| `labels` | `object` | User-defined labels. |
| `serviceClass` | `string` | Output only. The generated service class name. Use this name to refer to the Service class in Service Connection Maps and Service Connection Policies. |
| `updateTime` | `string` | Output only. Time when the ServiceClass was updated. |
| `createTime` | `string` | Output only. Time when the ServiceClass was created. |
| `etag` | `string` | Optional. The etag is computed by the server, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, serviceClassesId` | Gets details of a single ServiceClass. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists ServiceClasses in a given project and location. |
| `delete` | `DELETE` | `locationsId, projectsId, serviceClassesId` | Deletes a single ServiceClass. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists ServiceClasses in a given project and location. |
| `patch` | `EXEC` | `locationsId, projectsId, serviceClassesId` | Updates the parameters of a single ServiceClass. |
