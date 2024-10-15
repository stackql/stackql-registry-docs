---
title: identity_provider_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_provider_secrets
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

Creates, updates, deletes, gets or lists a <code>identity_provider_secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_provider_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.identity_provider_secrets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="clientSecret" /> | `string` | Client or app secret used in IdentityProviders, Aad, OpenID or OAuth. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="identityProviderName, resourceGroupName, serviceName, subscriptionId" /> | Gets the client secret details of the Identity Provider. |

## `SELECT` examples

Gets the client secret details of the Identity Provider.


```sql
SELECT
clientSecret
FROM azure.api_management.identity_provider_secrets
WHERE identityProviderName = '{{ identityProviderName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```