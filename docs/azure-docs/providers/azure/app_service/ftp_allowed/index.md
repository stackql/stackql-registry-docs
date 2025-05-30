---
title: ftp_allowed
hide_title: false
hide_table_of_contents: false
keywords:
  - ftp_allowed
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

Creates, updates, deletes, gets or lists a <code>ftp_allowed</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ftp_allowed</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.ftp_allowed" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | CsmPublishingCredentialsPoliciesEntity resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Returns whether FTP is allowed on the site or not. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Updates whether FTP is allowed on the site or not. |

## `SELECT` examples

Description for Returns whether FTP is allowed on the site or not.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.ftp_allowed
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `REPLACE` example

Replaces all fields in the specified <code>ftp_allowed</code> resource.

```sql
/*+ update */
REPLACE azure.app_service.ftp_allowed
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
