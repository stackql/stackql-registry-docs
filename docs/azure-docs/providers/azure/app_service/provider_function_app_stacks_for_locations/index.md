---
title: provider_function_app_stacks_for_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_function_app_stacks_for_locations
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

Creates, updates, deletes, gets or lists a <code>provider_function_app_stacks_for_locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_function_app_stacks_for_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.provider_function_app_stacks_for_locations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="location" /> | `string` | Function App stack location. |
| <CopyableCode code="properties" /> | `object` | FunctionAppStack resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location" /> | Description for Get available Function app frameworks and their versions for location |

## `SELECT` examples

Description for Get available Function app frameworks and their versions for location


```sql
SELECT
id,
name,
kind,
location,
properties,
type
FROM azure.app_service.provider_function_app_stacks_for_locations
WHERE location = '{{ location }}';
```