---
title: purview_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - purview_policies
  - purview_policy
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

Creates, updates, deletes, gets or lists a <code>purview_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>purview_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview_policy.purview_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="decisionRules" /> | `array` | Array of decision rules for the policy |
| <CopyableCode code="etag" /> | `string` | The etag version of a policy |
| <CopyableCode code="expiryTime" /> | `string` | The timestamp of the expiry time of the policy (UTC). |
| <CopyableCode code="kind" /> | `string` | The policy kind |
| <CopyableCode code="members" /> | `object` | Policy member |
| <CopyableCode code="requestor" /> | `string` | The AAD member who requested the policy |
| <CopyableCode code="scopes" /> | `array` | Array of scopes where the policy is published |
| <CopyableCode code="source" /> | `string` | The policy source |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | The API lists the Azure purview RBAC policies affecting the scope. The scope can be any valid ARM resource id |

## `SELECT` examples

The API lists the Azure purview RBAC policies affecting the scope. The scope can be any valid ARM resource id


```sql
SELECT
decisionRules,
etag,
expiryTime,
kind,
members,
requestor,
scopes,
source
FROM azure.purview_policy.purview_policies
WHERE scope = '{{ scope }}';
```