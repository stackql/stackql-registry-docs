---
title: provider_available_stacks_on_prem
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_available_stacks_on_prem
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

Creates, updates, deletes, gets or lists a <code>provider_available_stacks_on_prem</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_available_stacks_on_prem</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.provider_available_stacks_on_prem" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | Application stack. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Description for Get available application frameworks and their versions |

## `SELECT` examples

Description for Get available application frameworks and their versions


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.provider_available_stacks_on_prem
WHERE subscriptionId = '{{ subscriptionId }}';
```