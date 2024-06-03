---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - cloudcommerceprocurement
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudcommerceprocurement.accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the account. Account names have the form `accounts/&#123;account_id&#125;`. |
| <CopyableCode code="approvals" /> | `array` | Output only. The approvals for this account. These approvals are used to track actions that are permitted or have been completed by a customer within the context of the provider. This might include a sign up flow or a provisioning step, for example, that the provider can admit to having happened. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation timestamp. |
| <CopyableCode code="inputProperties" /> | `object` | Output only. The custom properties that were collected from the user to create this account. |
| <CopyableCode code="provider" /> | `string` | Output only. The identifier of the service provider that this account was created against. Each service provider is assigned a unique provider value when they onboard with Cloud Commerce platform. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the account. This is used to decide whether the customer is in good standing with the provider and is able to make purchases. An account might not be able to make a purchase if the billing account is suspended, for example. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update timestamp. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountsId, providersId" /> | Gets a requested Account resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="providersId" /> | Lists Accounts that the provider has access to. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="providersId" /> | Lists Accounts that the provider has access to. |
| <CopyableCode code="approve" /> | `EXEC` | <CopyableCode code="accountsId, providersId" /> | Grants an approval on an Account. |
| <CopyableCode code="reject" /> | `EXEC` | <CopyableCode code="accountsId, providersId" /> | Rejects an approval on an Account. |
| <CopyableCode code="reset" /> | `EXEC` | <CopyableCode code="accountsId, providersId" /> | Resets an Account and cancels all associated Entitlements. Partner can only reset accounts they own rather than customer accounts. |
