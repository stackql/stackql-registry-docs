---
title: registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - registrations
  - domains
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

Creates, updates, deletes or gets an <code>registration</code> resource or lists <code>registrations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.domains.registrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of the `Registration` resource, in the format `projects/*/locations/*/registrations/`. |
| <CopyableCode code="contactSettings" /> | `object` | Defines the contact information associated with a `Registration`. [ICANN](https://icann.org/) requires all domain names to have associated contact information. The `registrant_contact` is considered the domain's legal owner, and often the other contacts are identical. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation timestamp of the `Registration` resource. |
| <CopyableCode code="dnsSettings" /> | `object` | Defines the DNS configuration of a `Registration`, including name servers, DNSSEC, and glue records. |
| <CopyableCode code="domainName" /> | `string` | Required. Immutable. The domain name. Unicode domain names must be expressed in Punycode format. |
| <CopyableCode code="domainProperties" /> | `array` | Output only. Special properties of the domain. |
| <CopyableCode code="expireTime" /> | `string` | Output only. The expiration timestamp of the `Registration`. |
| <CopyableCode code="issues" /> | `array` | Output only. The set of issues with the `Registration` that require attention. |
| <CopyableCode code="labels" /> | `object` | Set of labels associated with the `Registration`. |
| <CopyableCode code="managementSettings" /> | `object` | Defines renewal, billing, and transfer settings for a `Registration`. |
| <CopyableCode code="pendingContactSettings" /> | `object` | Defines the contact information associated with a `Registration`. [ICANN](https://icann.org/) requires all domain names to have associated contact information. The `registrant_contact` is considered the domain's legal owner, and often the other contacts are identical. |
| <CopyableCode code="registerFailureReason" /> | `string` | Output only. The reason the domain registration failed. Only set for domains in REGISTRATION_FAILED state. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the `Registration` |
| <CopyableCode code="supportedPrivacy" /> | `array` | Output only. Set of options for the `contact_settings.privacy` field that this `Registration` supports. |
| <CopyableCode code="transferFailureReason" /> | `string` | Output only. Deprecated: For more information, see [Cloud Domains feature deprecation](https://cloud.google.com/domains/docs/deprecations/feature-deprecations). The reason the domain transfer failed. Only set for domains in TRANSFER_FAILED state. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, registrationsId" /> | Gets the details of a `Registration` resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists the `Registration` resources in a project. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, registrationsId" /> | Deletes a `Registration` resource. This method works on any `Registration` resource using [Subscription or Commitment billing](/domains/pricing#billing-models), provided that the resource was created at least 1 day in the past. When an active registration is successfully deleted, you can continue to use the domain in [Google Domains](https://domains.google/) until it expires. The calling user becomes the domain's sole owner in Google Domains, and permissions for the domain are subsequently managed there. The domain does not renew automatically unless the new owner sets up billing in Google Domains. After January 2024 you will only be able to delete `Registration` resources when `state` is one of: `EXPORTED`, `EXPIRED`,`REGISTRATION_FAILED` or `TRANSFER_FAILED`. See [Cloud Domains feature deprecation](https://cloud.google.com/domains/docs/deprecations/feature-deprecations) for more details. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, registrationsId" /> | Updates select fields of a `Registration` resource, notably `labels`. To update other fields, use the appropriate custom update method: * To update management settings, see `ConfigureManagementSettings` * To update DNS configuration, see `ConfigureDnsSettings` * To update contact information, see `ConfigureContactSettings` |
| <CopyableCode code="configure_contact_settings" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, registrationsId" /> | Updates a `Registration`'s contact settings. Some changes require confirmation by the domain's registrant contact . Caution: Please consider carefully any changes to contact privacy settings when changing from `REDACTED_CONTACT_DATA` to `PUBLIC_CONTACT_DATA.` There may be a delay in reflecting updates you make to registrant contact information such that any changes you make to contact privacy (including from `REDACTED_CONTACT_DATA` to `PUBLIC_CONTACT_DATA`) will be applied without delay but changes to registrant contact information may take a limited time to be publicized. This means that changes to contact privacy from `REDACTED_CONTACT_DATA` to `PUBLIC_CONTACT_DATA` may make the previous registrant contact data public until the modified registrant contact details are published. |
| <CopyableCode code="configure_dns_settings" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, registrationsId" /> | Updates a `Registration`'s DNS settings. |
| <CopyableCode code="configure_management_settings" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, registrationsId" /> | Updates a `Registration`'s management settings. |
| <CopyableCode code="export" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, registrationsId" /> | Deprecated: For more information, see [Cloud Domains feature deprecation](https://cloud.google.com/domains/docs/deprecations/feature-deprecations) Exports a `Registration` resource, such that it is no longer managed by Cloud Domains. When an active domain is successfully exported, you can continue to use the domain in [Google Domains](https://domains.google/) until it expires. The calling user becomes the domain's sole owner in Google Domains, and permissions for the domain are subsequently managed there. The domain does not renew automatically unless the new owner sets up billing in Google Domains. |
| <CopyableCode code="import" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Deprecated: For more information, see [Cloud Domains feature deprecation](https://cloud.google.com/domains/docs/deprecations/feature-deprecations) Imports a domain name from [Google Domains](https://domains.google/) for use in Cloud Domains. To transfer a domain from another registrar, use the `TransferDomain` method instead. Since individual users can own domains in Google Domains, the calling user must have ownership permission on the domain. |
| <CopyableCode code="initiate_push_transfer" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, registrationsId" /> | Initiates the `Push Transfer` process to transfer the domain to another registrar. The process might complete instantly or might require confirmation or additional work. Check the emails sent to the email address of the registrant. The process is aborted after a timeout if it's not completed. This method is only supported for domains that have the `REQUIRE_PUSH_TRANSFER` property in the list of `domain_properties`. The domain must also be unlocked before it can be transferred to a different registrar. For more information, see [Transfer a registered domain to another registrar](https://cloud.google.com/domains/docs/transfer-domain-to-another-registrar). |
| <CopyableCode code="register" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Registers a new domain name and creates a corresponding `Registration` resource. Call `RetrieveRegisterParameters` first to check availability of the domain name and determine parameters like price that are needed to build a call to this method. A successful call creates a `Registration` resource in state `REGISTRATION_PENDING`, which resolves to `ACTIVE` within 1-2 minutes, indicating that the domain was successfully registered. If the resource ends up in state `REGISTRATION_FAILED`, it indicates that the domain was not registered successfully, and you can safely delete the resource and retry registration. |
| <CopyableCode code="renew_domain" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, registrationsId" /> | Renews a recently expired domain. This method can only be called on domains that expired in the previous 30 days. After the renewal, the new expiration time of the domain is one year after the old expiration time and you are charged a `yearly_price` for the renewal. |
| <CopyableCode code="reset_authorization_code" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, registrationsId" /> | Resets the authorization code of the `Registration` to a new random string. You can call this method only after 60 days have elapsed since the initial domain registration. Domains that have the `REQUIRE_PUSH_TRANSFER` property in the list of `domain_properties` don't support authorization codes and must use the `InitiatePushTransfer` method to initiate the process to transfer the domain to a different registrar. |
| <CopyableCode code="search_domains" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Searches for available domain names similar to the provided query. Availability results from this method are approximate; call `RetrieveRegisterParameters` on a domain before registering to confirm availability. |
| <CopyableCode code="transfer" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Deprecated: For more information, see [Cloud Domains feature deprecation](https://cloud.google.com/domains/docs/deprecations/feature-deprecations) Transfers a domain name from another registrar to Cloud Domains. For domains already managed by [Google Domains](https://domains.google/), use `ImportDomain` instead. Before calling this method, go to the domain's current registrar to unlock the domain for transfer and retrieve the domain's transfer authorization code. Then call `RetrieveTransferParameters` to confirm that the domain is unlocked and to get values needed to build a call to this method. A successful call creates a `Registration` resource in state `TRANSFER_PENDING`. It can take several days to complete the transfer process. The registrant can often speed up this process by approving the transfer through the current registrar, either by clicking a link in an email from the registrar or by visiting the registrar's website. A few minutes after transfer approval, the resource transitions to state `ACTIVE`, indicating that the transfer was successful. If the transfer is rejected or the request expires without being approved, the resource can end up in state `TRANSFER_FAILED`. If transfer fails, you can safely delete the resource and retry the transfer. |

## `SELECT` examples

Lists the `Registration` resources in a project.

```sql
SELECT
name,
contactSettings,
createTime,
dnsSettings,
domainName,
domainProperties,
expireTime,
issues,
labels,
managementSettings,
pendingContactSettings,
registerFailureReason,
state,
supportedPrivacy,
transferFailureReason
FROM google.domains.registrations
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `UPDATE` example

Updates a registration only if the necessary resources are available.

```sql
UPDATE google.domains.registrations
SET 
name = '{{ name }}',
domainName = '{{ domainName }}',
createTime = '{{ createTime }}',
expireTime = '{{ expireTime }}',
state = '{{ state }}',
issues = '{{ issues }}',
labels = '{{ labels }}',
managementSettings = '{{ managementSettings }}',
dnsSettings = '{{ dnsSettings }}',
contactSettings = '{{ contactSettings }}',
pendingContactSettings = '{{ pendingContactSettings }}',
supportedPrivacy = '{{ supportedPrivacy }}',
registerFailureReason = '{{ registerFailureReason }}',
transferFailureReason = '{{ transferFailureReason }}',
domainProperties = '{{ domainProperties }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND registrationsId = '{{ registrationsId }}';
```

## `DELETE` example

Deletes the specified registration resource.

```sql
DELETE FROM google.domains.registrations
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND registrationsId = '{{ registrationsId }}';
```
