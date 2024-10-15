---
title: private_link_resources_slots
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_resources_slots
  - app_service
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

Creates, updates, deletes, gets or lists a <code>private_link_resources_slots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_link_resources_slots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.private_link_resources_slots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` | Name of a private link resource |
| <CopyableCode code="properties" /> | `object` | Properties of a private link resource |
| <CopyableCode code="type" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Gets the private link resources |

## `SELECT` examples

Description for Gets the private link resources


```sql
SELECT
id,
name,
properties,
type
FROM azure.app_service.private_link_resources_slots
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```