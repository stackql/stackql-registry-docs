
---
title: status
hide_title: false
hide_table_of_contents: false
keywords:
  - status
  - contentwarehouse
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

Creates, updates, deletes or gets an <code>status</code> resource or lists <code>status</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.contentwarehouse.status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accessControlMode" /> | `string` | Access control mode. |
| <CopyableCode code="databaseType" /> | `string` | Database type. |
| <CopyableCode code="documentCreatorDefaultRole" /> | `string` | The default role for the person who create a document. |
| <CopyableCode code="location" /> | `string` | The location of the queried project. |
| <CopyableCode code="qaEnabled" /> | `boolean` | If the qa is enabled on this project. |
| <CopyableCode code="state" /> | `string` | State of the project. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_status" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Get the project status. |

## `SELECT` examples

Get the project status.

```sql
SELECT
accessControlMode,
databaseType,
documentCreatorDefaultRole,
location,
qaEnabled,
state
FROM google.contentwarehouse.status
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
