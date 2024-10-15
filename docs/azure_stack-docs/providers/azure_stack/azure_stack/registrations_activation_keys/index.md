---
title: registrations_activation_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - registrations_activation_keys
  - azure_stack
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

Creates, updates, deletes, gets or lists a <code>registrations_activation_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registrations_activation_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack.registrations_activation_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="activationKey" /> | `string` | Azure Stack activation key. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="registrationName, resourceGroup, subscriptionId" /> | Returns Azure Stack Activation Key. |

## `SELECT` examples

Returns Azure Stack Activation Key.


```sql
SELECT
activationKey
FROM azure_stack.azure_stack.registrations_activation_keys
WHERE registrationName = '{{ registrationName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}';
```