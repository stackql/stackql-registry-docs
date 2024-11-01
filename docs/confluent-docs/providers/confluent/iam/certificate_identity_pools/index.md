---
title: certificate_identity_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_identity_pools
  - iam
  - confluent    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Confluent Cloud resources using SQL.
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_identity_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.iam.certificate_identity_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="description" /> | `string` | A description of how this `IdentityPool` is used |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="display_name" /> | `string` | The name of the `IdentityPool`. |
| <CopyableCode code="external_identifier" /> | `string` | The certificate field that will be used to represent the<br />pool's external identifier for audit logging. |
| <CopyableCode code="filter" /> | `string` | A filter expression in [Supported Common Expression Language (CEL)](https://docs.confluent.io/cloud/current/access-management/authenticate/mtls/cel-filters.html) that specifies which identities can authenticate using your certificate identity pool (see [CEL filter for mTLS](https://docs.confluent.io/cloud/current/access-management/authenticate/mtls/cel-filters.html) for more details). |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="principal" /> | `string` | Represents the federated identity associated with this pool. |
| <CopyableCode code="state" /> | `string` | The current state of the identity pool |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_iam_v2certificate_identity_pool" /> | `SELECT` | <CopyableCode code="certificate_authority_id, id" /> | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to read a certificate identity pool. |
| <CopyableCode code="list_iam_v2certificate_identity_pools" /> | `SELECT` | <CopyableCode code="certificate_authority_id" /> | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Retrieve a sorted, filtered, paginated list of all certificate identity pools. |
| <CopyableCode code="create_iam_v2certificate_identity_pool" /> | `INSERT` | <CopyableCode code="certificate_authority_id" /> | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to create a certificate identity pool. |
| <CopyableCode code="delete_iam_v2certificate_identity_pool" /> | `DELETE` | <CopyableCode code="certificate_authority_id, id" /> | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to delete a certificate identity pool. |
| <CopyableCode code="update_iam_v2certificate_identity_pool" /> | `EXEC` | <CopyableCode code="certificate_authority_id, id" /> | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to update a certificate identity pool.<br /><br /> |
