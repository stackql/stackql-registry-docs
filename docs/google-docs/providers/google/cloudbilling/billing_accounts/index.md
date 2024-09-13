---
title: billing_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_accounts
  - cloudbilling
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

Creates, updates, deletes, gets or lists a <code>billing_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>billing_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudbilling.billing_accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the billing account. The resource name has the form `billingAccounts/{billing_account_id}`. For example, `billingAccounts/012345-567890-ABCDEF` would be the resource name for billing account `012345-567890-ABCDEF`. |
| <CopyableCode code="displayName" /> | `string` | The display name given to the billing account, such as `My Billing Account`. This name is displayed in the Google Cloud Console. |
| <CopyableCode code="masterBillingAccount" /> | `string` | If this account is a [subaccount](https://cloud.google.com/billing/docs/concepts), then this will be the resource name of the parent billing account that it is being resold through. Otherwise this will be empty. |
| <CopyableCode code="open" /> | `boolean` | Output only. True if the billing account is open, and will therefore be charged for any usage on associated projects. False if the billing account is closed, and therefore projects associated with it are unable to use paid services. |
| <CopyableCode code="parent" /> | `string` | Output only. The billing account's parent resource identifier. Use the `MoveBillingAccount` method to update the account's parent resource if it is a organization. Format: - `organizations/{organization_id}`, for example, `organizations/12345678` - `billingAccounts/{billing_account_id}`, for example, `billingAccounts/012345-567890-ABCDEF` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="billingAccountsId" /> | Gets information about a billing account. The current authenticated user must be a [viewer of the billing account](https://cloud.google.com/billing/docs/how-to/billing-access). |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists the billing accounts that the current authenticated user has permission to [view](https://cloud.google.com/billing/docs/how-to/billing-access). |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | This method creates [billing subaccounts](https://cloud.google.com/billing/docs/concepts#subaccounts). Google Cloud resellers should use the Channel Services APIs, [accounts.customers.create](https://cloud.google.com/channel/docs/reference/rest/v1/accounts.customers/create) and [accounts.customers.entitlements.create](https://cloud.google.com/channel/docs/reference/rest/v1/accounts.customers.entitlements/create). When creating a subaccount, the current authenticated user must have the `billing.accounts.update` IAM permission on the parent account, which is typically given to billing account [administrators](https://cloud.google.com/billing/docs/how-to/billing-access). This method will return an error if the parent account has not been provisioned for subaccounts. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="billingAccountsId" /> | Updates a billing account's fields. Currently the only field that can be edited is `display_name`. The current authenticated user must have the `billing.accounts.update` IAM permission, which is typically given to the [administrator](https://cloud.google.com/billing/docs/how-to/billing-access) of the billing account. |
| <CopyableCode code="move" /> | `EXEC` | <CopyableCode code="billingAccountsId, organizationsId" /> | Changes which parent organization a billing account belongs to. |

## `SELECT` examples

Lists the billing accounts that the current authenticated user has permission to [view](https://cloud.google.com/billing/docs/how-to/billing-access).

```sql
SELECT
name,
displayName,
masterBillingAccount,
open,
parent
FROM google.cloudbilling.billing_accounts
WHERE organizationsId = '{{ organizationsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>billing_accounts</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.cloudbilling.billing_accounts (
organizationsId,
name,
open,
displayName,
masterBillingAccount,
parent
)
SELECT 
'{{ organizationsId }}',
'{{ name }}',
true|false,
'{{ displayName }}',
'{{ masterBillingAccount }}',
'{{ parent }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: open
        value: '{{ open }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: masterBillingAccount
        value: '{{ masterBillingAccount }}'
      - name: parent
        value: '{{ parent }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>billing_accounts</code> resource.

```sql
/*+ update */
UPDATE google.cloudbilling.billing_accounts
SET 
name = '{{ name }}',
open = true|false,
displayName = '{{ displayName }}',
masterBillingAccount = '{{ masterBillingAccount }}',
parent = '{{ parent }}'
WHERE 
billingAccountsId = '{{ billingAccountsId }}';
```
