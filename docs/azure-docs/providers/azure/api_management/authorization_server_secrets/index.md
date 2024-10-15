---
title: authorization_server_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization_server_secrets
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

Creates, updates, deletes, gets or lists a <code>authorization_server_secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorization_server_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.authorization_server_secrets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="clientSecret" /> | `string` | oAuth Authorization Server Secrets. |
| <CopyableCode code="resourceOwnerPassword" /> | `string` | Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner password. |
| <CopyableCode code="resourceOwnerUsername" /> | `string` | Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner username. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="authsid, resourceGroupName, serviceName, subscriptionId" /> | Gets the client secret details of the authorization server. |

## `SELECT` examples

Gets the client secret details of the authorization server.


```sql
SELECT
clientSecret,
resourceOwnerPassword,
resourceOwnerUsername
FROM azure.api_management.authorization_server_secrets
WHERE authsid = '{{ authsid }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```