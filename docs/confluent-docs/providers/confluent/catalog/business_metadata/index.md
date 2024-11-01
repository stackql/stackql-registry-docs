---
title: business_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - business_metadata
  - catalog
  - confluent    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Confluent Cloud resources using SQL.
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>business_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.catalog.business_metadata" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="attributes" /> | `object` | The business metadata attributes |
| <CopyableCode code="entityName" /> | `string` | The qualified name of the entity |
| <CopyableCode code="entityType" /> | `string` | The entity type |
| <CopyableCode code="error" /> | `object` | Error message of this operation |
| <CopyableCode code="typeName" /> | `string` | The business metadata name |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_business_metadata" /> | `SELECT` | <CopyableCode code="qualifiedName, typeName" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Gets the list of business metadata for a given entity represented<br />by a qualified name. |
| <CopyableCode code="create_business_metadata" /> | `INSERT` |  | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Bulk API to create multiple business metadata. |
| <CopyableCode code="delete_business_metadata" /> | `DELETE` | <CopyableCode code="bmName, qualifiedName, typeName" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Delete a business metadata on an entity. |
| <CopyableCode code="update_business_metadata" /> | `EXEC` |  | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Bulk API to update multiple business metadata. |
