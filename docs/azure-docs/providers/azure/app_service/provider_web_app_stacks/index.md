---
title: provider_web_app_stacks
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_web_app_stacks
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

Creates, updates, deletes, gets or lists a <code>provider_web_app_stacks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_web_app_stacks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.provider_web_app_stacks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="location" /> | `string` | Web App stack location. |
| <CopyableCode code="properties" /> | `object` | WebAppStack resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="" /> | Description for Get available Web app frameworks and their versions |

## `SELECT` examples

Description for Get available Web app frameworks and their versions


```sql
SELECT
id,
name,
kind,
location,
properties,
type
FROM azure.app_service.provider_web_app_stacks
;
```