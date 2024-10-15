---
title: service_sso_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - service_sso_tokens
  - api_management
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

Creates, updates, deletes, gets or lists a <code>service_sso_tokens</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_sso_tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.service_sso_tokens" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="redirectUri" /> | `string` | Redirect URL to the Publisher Portal containing the SSO token. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Gets the Single-Sign-On token for the API Management Service which is valid for 5 Minutes. |

## `SELECT` examples

Gets the Single-Sign-On token for the API Management Service which is valid for 5 Minutes.


```sql
SELECT
redirectUri
FROM azure.api_management.service_sso_tokens
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```