---
title: object_data_types_fields_by_module_and_types
hide_title: false
hide_table_of_contents: false
keywords:
  - object_data_types_fields_by_module_and_types
  - automation
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>object_data_types_fields_by_module_and_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>object_data_types_fields_by_module_and_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.object_data_types_fields_by_module_and_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Gets or sets the name of the field. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type of the field. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="automationAccountName, moduleName, resourceGroupName, subscriptionId, typeName" /> | Retrieve a list of fields of a given type identified by module name. |

## `SELECT` examples

Retrieve a list of fields of a given type identified by module name.


```sql
SELECT
name,
type
FROM azure.automation.object_data_types_fields_by_module_and_types
WHERE automationAccountName = '{{ automationAccountName }}'
AND moduleName = '{{ moduleName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND typeName = '{{ typeName }}';
```