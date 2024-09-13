
---
title: memberships
hide_title: false
hide_table_of_contents: false
keywords:
  - memberships
  - recaptchaenterprise
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

Creates, updates, deletes or gets an <code>membership</code> resource or lists <code>memberships</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>memberships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.recaptchaenterprise.memberships" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Identifier. The resource name for this membership in the format `projects/{project}/relatedaccountgroups/{relatedaccountgroup}/memberships/{membership}`. |
| <CopyableCode code="accountId" /> | `string` | The unique stable account identifier of the member. The identifier corresponds to an `account_id` provided in a previous `CreateAssessment` or `AnnotateAssessment` call. |
| <CopyableCode code="hashedAccountId" /> | `string` | Deprecated: use `account_id` instead. The unique stable hashed account identifier of the member. The identifier corresponds to a `hashed_account_id` provided in a previous `CreateAssessment` or `AnnotateAssessment` call. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId, relatedaccountgroupsId" /> | Get memberships in a group of related accounts. |

## `SELECT` examples

Get memberships in a group of related accounts.

```sql
SELECT
name,
accountId,
hashedAccountId
FROM google.recaptchaenterprise.memberships
WHERE projectsId = '{{ projectsId }}'
AND relatedaccountgroupsId = '{{ relatedaccountgroupsId }}'; 
```
