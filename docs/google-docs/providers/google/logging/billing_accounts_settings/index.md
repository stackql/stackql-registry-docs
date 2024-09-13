
---
title: billing_accounts_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_accounts_settings
  - logging
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

Creates, updates, deletes or gets an <code>billing_accounts_setting</code> resource or lists <code>billing_accounts_settings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>billing_accounts_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.logging.billing_accounts_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the settings. |
| <CopyableCode code="defaultSinkConfig" /> | `object` | Describes the custom _Default sink configuration that is used to override the built-in _Default sink configuration in newly created resource containers, such as projects or folders. |
| <CopyableCode code="disableDefaultSink" /> | `boolean` | Optional. If set to true, the _Default sink in newly created projects and folders will created in a disabled state. This can be used to automatically disable log storage if there is already an aggregated sink configured in the hierarchy. The _Default sink can be re-enabled manually if needed. |
| <CopyableCode code="kmsKeyName" /> | `string` | Optional. The resource name for the configured Cloud KMS key.KMS key name format: "projects/[PROJECT_ID]/locations/[LOCATION]/keyRings/[KEYRING]/cryptoKeys/[KEY]" For example:"projects/my-project/locations/us-central1/keyRings/my-ring/cryptoKeys/my-key"To enable CMEK, set this field to a valid kms_key_name for which the associated service account has the required roles/cloudkms.cryptoKeyEncrypterDecrypter role assigned for the key.The Cloud KMS key used by the Log Router can be updated by changing the kms_key_name to a new valid key name.To disable CMEK for the Log Router, set this field to an empty string.See Enabling CMEK for Log Router (https://cloud.google.com/logging/docs/routing/managed-encryption) for more information. |
| <CopyableCode code="kmsServiceAccountId" /> | `string` | Output only. The service account that will be used by the Log Router to access your Cloud KMS key.Before enabling CMEK, you must first assign the role roles/cloudkms.cryptoKeyEncrypterDecrypter to the service account that will be used to access your Cloud KMS key. Use GetSettings to obtain the service account ID.See Enabling CMEK for Log Router (https://cloud.google.com/logging/docs/routing/managed-encryption) for more information. |
| <CopyableCode code="loggingServiceAccountId" /> | `string` | Output only. The service account for the given resource container, such as project or folder. Log sinks use this service account as their writer_identity if no custom service account is provided in the request when calling the create sink method. |
| <CopyableCode code="storageLocation" /> | `string` | Optional. The storage location for the _Default and _Required log buckets of newly created projects and folders, unless the storage location is explicitly provided.Example value: europe-west1.Note: this setting does not affect the location of resources where a location is explicitly provided when created, such as custom log buckets. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="billing_accounts_get_settings" /> | `SELECT` | <CopyableCode code="billingAccountsId" /> | Gets the settings for the given resource.Note: Settings can be retrieved for Google Cloud projects, folders, organizations, and billing accounts.See View default resource settings for Logging (https://cloud.google.com/logging/docs/default-settings#view-org-settings) for more information. |

## `SELECT` examples

Gets the settings for the given resource.Note: Settings can be retrieved for Google Cloud projects, folders, organizations, and billing accounts.See View default resource settings for Logging (https://cloud.google.com/logging/docs/default-settings#view-org-settings) for more information.

```sql
SELECT
name,
defaultSinkConfig,
disableDefaultSink,
kmsKeyName,
kmsServiceAccountId,
loggingServiceAccountId,
storageLocation
FROM google.logging.billing_accounts_settings
WHERE billingAccountsId = '{{ billingAccountsId }}'; 
```
