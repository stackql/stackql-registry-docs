---
title: provider_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_operations
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

Creates, updates, deletes, gets or lists a <code>provider_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.provider_operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="display" /> | `object` | Meta data about operation used for display in portal. |
| <CopyableCode code="isDataAction" /> | `boolean` |  |
| <CopyableCode code="origin" /> | `string` |  |
| <CopyableCode code="properties" /> | `object` | Properties available for a Microsoft.Web resource provider operation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Description for Gets all available operations for the Microsoft.Web resource provider. Also exposes resource metric definitions |

## `SELECT` examples

Description for Gets all available operations for the Microsoft.Web resource provider. Also exposes resource metric definitions


```sql
SELECT
name,
display,
isDataAction,
origin,
properties
FROM azure.app_service.provider_operations
;
```