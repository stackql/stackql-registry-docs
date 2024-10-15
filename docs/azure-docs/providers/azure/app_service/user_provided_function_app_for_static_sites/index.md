---
title: user_provided_function_app_for_static_sites
hide_title: false
hide_table_of_contents: false
keywords:
  - user_provided_function_app_for_static_sites
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

Creates, updates, deletes, gets or lists a <code>user_provided_function_app_for_static_sites</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_provided_function_app_for_static_sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.user_provided_function_app_for_static_sites" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | StaticSiteUserProvidedFunctionAppARMResource resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="functionAppName, name, resourceGroupName, subscriptionId" /> | Description for Gets the details of the user provided function app registered with a static site |

## `SELECT` examples

Description for Gets the details of the user provided function app registered with a static site


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.user_provided_function_app_for_static_sites
WHERE functionAppName = '{{ functionAppName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```