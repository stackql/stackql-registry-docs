---
title: tag_defs
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_defs
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
<tr><td><b>Name</b></td><td><code>tag_defs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.catalog.tag_defs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name |
| <CopyableCode code="description" /> | `string` | The description |
| <CopyableCode code="attributeDefs" /> | `array` | The attribute definitions |
| <CopyableCode code="category" /> | `string` | The category |
| <CopyableCode code="createTime" /> | `integer` | The create time |
| <CopyableCode code="createdBy" /> | `string` | The creator |
| <CopyableCode code="entityTypes" /> | `array` | The entity types |
| <CopyableCode code="guid" /> | `string` | The internal guid |
| <CopyableCode code="options" /> | `object` | The options |
| <CopyableCode code="serviceType" /> | `string` | The service type |
| <CopyableCode code="subTypes" /> | `array` | The subtypes |
| <CopyableCode code="superTypes" /> | `array` | The supertypes |
| <CopyableCode code="typeVersion" /> | `string` | The type version |
| <CopyableCode code="updateTime" /> | `integer` | The update time |
| <CopyableCode code="updatedBy" /> | `string` | The updater |
| <CopyableCode code="version" /> | `integer` | The version |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_all_tag_defs" /> | `SELECT` |  | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Bulk retrieval API for retrieving tag definitions. |
| <CopyableCode code="get_tag_def_by_name" /> | `SELECT` | <CopyableCode code="tagName" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Get the tag definition with the given name. |
| <CopyableCode code="create_tag_defs" /> | `INSERT` |  | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Bulk create API for tag definitions. |
| <CopyableCode code="delete_tag_def" /> | `DELETE` | <CopyableCode code="tagName" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Delete API for tag definition identified by its name. |
| <CopyableCode code="update_tag_defs" /> | `EXEC` |  | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Bulk update API for tag definitions. |
