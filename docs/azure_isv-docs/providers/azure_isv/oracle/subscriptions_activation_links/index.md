---
title: subscriptions_activation_links
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions_activation_links
  - oracle
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

Creates, updates, deletes, gets or lists a <code>subscriptions_activation_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriptions_activation_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.subscriptions_activation_links" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="existingCloudAccountActivationLink" /> | `string` | Existing Cloud Account Activation Link |
| <CopyableCode code="newCloudAccountActivationLink" /> | `string` | New Cloud Account Activation Link |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List Activation Links |

## `SELECT` examples

List Activation Links


```sql
SELECT
existingCloudAccountActivationLink,
newCloudAccountActivationLink
FROM azure_isv.oracle.subscriptions_activation_links
WHERE subscriptionId = '{{ subscriptionId }}';
```