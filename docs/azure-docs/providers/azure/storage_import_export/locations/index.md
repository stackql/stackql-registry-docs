---
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
  - storage_import_export
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_import_export.locations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Specifies the resource identifier of the location.  |
| <CopyableCode code="name" /> | `string` | Specifies the name of the location. Use List Locations to get all supported locations.  |
| <CopyableCode code="properties" /> | `` | location properties |
| <CopyableCode code="type" /> | `string` | Specifies the type of the location.  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, locationName" /> | Returns the details about a location to which you can ship the disks associated with an import or export job. A location is an Azure region. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version" /> | Returns a list of locations to which you can ship the disks associated with an import or export job. A location is a Microsoft data center region. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version" /> | Returns a list of locations to which you can ship the disks associated with an import or export job. A location is a Microsoft data center region. |
