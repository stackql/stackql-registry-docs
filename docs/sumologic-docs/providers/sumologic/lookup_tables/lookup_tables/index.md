---
title: lookup_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - lookup_tables
  - lookup_tables
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>lookup_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.lookup_tables.lookup_tables" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="createTable" /> | `INSERT` | <CopyableCode code="data__name, data__parentFolderId, region" /> | Create a new lookup table by providing a schema and specifying its configuration. Providing parentFolderId<br /> is mandatory. Use the [getItemByPath](#operation/getItemByPath) endpoint to get content id of a path.<br />Please check [Content management API](#tag/contentManagement) and [Folder management API](#tag/folderManagement) for all available options. |
| <CopyableCode code="deleteTable" /> | `DELETE` | <CopyableCode code="id, region" /> | Delete a lookup table completely. &lt;br&gt; **Warning:** `This operation cannot be undone`. |
| <CopyableCode code="lookupTableById" /> | `EXEC` | <CopyableCode code="id, region" /> | Get a lookup table for the given identifier. |
| <CopyableCode code="updateTable" /> | `EXEC` | <CopyableCode code="id, data__description, data__ttl, region" /> | Edit the lookup table data. All the fields are mandatory in the request. |
