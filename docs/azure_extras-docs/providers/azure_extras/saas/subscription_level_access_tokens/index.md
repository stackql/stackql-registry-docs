---
title: subscription_level_access_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription_level_access_tokens
  - saas
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

Creates, updates, deletes, gets or lists a <code>subscription_level_access_tokens</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscription_level_access_tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.saas.subscription_level_access_tokens" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="publisherOfferBaseUri" /> | `string` | The Publisher Offer Base Uri |
| <CopyableCode code="token" /> | `string` | The generated token |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets the ISV access token for a specified Subscription Level SaaS. |

## `SELECT` examples

Gets the ISV access token for a specified Subscription Level SaaS.


```sql
SELECT
publisherOfferBaseUri,
token
FROM azure_extras.saas.subscription_level_access_tokens
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```