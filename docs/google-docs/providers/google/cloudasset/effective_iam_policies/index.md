---
title: effective_iam_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - effective_iam_policies
  - cloudasset
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

Creates, updates, deletes, gets or lists a <code>effective_iam_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>effective_iam_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudasset.effective_iam_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="policyResults" /> | `array` | The effective policies for a batch of resources. Note that the results order is the same as the order of BatchGetEffectiveIamPoliciesRequest.names. When a resource does not have any effective IAM policies, its corresponding policy_result will contain empty EffectiveIamPolicy.policies. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="batch_get" /> | `SELECT` | <CopyableCode code="scope" /> | Gets effective IAM policies for a batch of resources. |

## `SELECT` examples

Gets effective IAM policies for a batch of resources.

```sql
SELECT
policyResults
FROM google.cloudasset.effective_iam_policies
WHERE scope = '{{ scope }}';
```
