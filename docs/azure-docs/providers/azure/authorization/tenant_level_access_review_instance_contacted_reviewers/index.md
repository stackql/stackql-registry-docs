---
title: tenant_level_access_review_instance_contacted_reviewers
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_level_access_review_instance_contacted_reviewers
  - authorization
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

Creates, updates, deletes, gets or lists a <code>tenant_level_access_review_instance_contacted_reviewers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tenant_level_access_review_instance_contacted_reviewers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.tenant_level_access_review_instance_contacted_reviewers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The access review reviewer id. |
| <CopyableCode code="name" /> | `string` | The access review reviewer id. |
| <CopyableCode code="properties" /> | `object` | Properties of access review contacted reviewer. |
| <CopyableCode code="type" /> | `string` | The resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="id, scheduleDefinitionId" /> | Get access review instance contacted reviewers |

## `SELECT` examples

Get access review instance contacted reviewers


```sql
SELECT
id,
name,
properties,
type
FROM azure.authorization.tenant_level_access_review_instance_contacted_reviewers
WHERE id = '{{ id }}'
AND scheduleDefinitionId = '{{ scheduleDefinitionId }}';
```