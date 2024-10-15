---
title: resource_guards_delete_resource_guard_proxy_requests_objects
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_guards_delete_resource_guard_proxy_requests_objects
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

Creates, updates, deletes, gets or lists a <code>resource_guards_delete_resource_guard_proxy_requests_objects</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_guards_delete_resource_guard_proxy_requests_objects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_protection.resource_guards_delete_resource_guard_proxy_requests_objects" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id represents the complete path to the resource. |
| <CopyableCode code="name" /> | `string` | Resource name associated with the resource. |
| <CopyableCode code="type" /> | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceGuardsName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
id,
name,
type
FROM azure.data_protection.resource_guards_delete_resource_guard_proxy_requests_objects
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceGuardsName = '{{ resourceGuardsName }}'
AND subscriptionId = '{{ subscriptionId }}';
```