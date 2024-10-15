---
title: content_key_policies_policy_properties_with_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - content_key_policies_policy_properties_with_secrets
  - media_services
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

Creates, updates, deletes, gets or lists a <code>content_key_policies_policy_properties_with_secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>content_key_policies_policy_properties_with_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.content_key_policies_policy_properties_with_secrets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | A description for the Policy. |
| <CopyableCode code="created" /> | `string` | The creation date of the Policy |
| <CopyableCode code="lastModified" /> | `string` | The last modified date of the Policy |
| <CopyableCode code="options" /> | `array` | The Key Policy options. |
| <CopyableCode code="policyId" /> | `string` | The legacy Policy ID. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, contentKeyPolicyName, resourceGroupName, subscriptionId" /> | Get a Content Key Policy including secret values |

## `SELECT` examples

Get a Content Key Policy including secret values


```sql
SELECT
description,
created,
lastModified,
options,
policyId
FROM azure.media_services.content_key_policies_policy_properties_with_secrets
WHERE accountName = '{{ accountName }}'
AND contentKeyPolicyName = '{{ contentKeyPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```