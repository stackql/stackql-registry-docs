---
title: backup_instances_extension_routings
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_instances_extension_routings
  - data_protection
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

Creates, updates, deletes, gets or lists a <code>backup_instances_extension_routings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_instances_extension_routings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_protection.backup_instances_extension_routings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Proxy Resource Id represents the complete path to the resource. |
| <CopyableCode code="name" /> | `string` | Proxy Resource name associated with the resource. |
| <CopyableCode code="properties" /> | `object` | Backup Instance |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Proxy Resource tags. |
| <CopyableCode code="type" /> | `string` | Proxy Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceId" /> | Gets a list of backup instances associated with a tracked resource |

## `SELECT` examples

Gets a list of backup instances associated with a tracked resource


```sql
SELECT
id,
name,
properties,
systemData,
tags,
type
FROM azure.data_protection.backup_instances_extension_routings
WHERE resourceId = '{{ resourceId }}';
```