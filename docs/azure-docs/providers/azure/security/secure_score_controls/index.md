---
title: secure_score_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - secure_score_controls
  - security
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

Creates, updates, deletes, gets or lists a <code>secure_score_controls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secure_score_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.secure_score_controls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Calculation result data in control level |
| <CopyableCode code="type" /> | `string` | Resource type |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get all security controls within a scope |
| <CopyableCode code="list_by_secure_score" /> | `SELECT` | <CopyableCode code="secureScoreName, subscriptionId" /> | Get all security controls for a specific initiative within a scope |

## `SELECT` examples

Get all security controls within a scope


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.secure_score_controls
WHERE subscriptionId = '{{ subscriptionId }}';
```