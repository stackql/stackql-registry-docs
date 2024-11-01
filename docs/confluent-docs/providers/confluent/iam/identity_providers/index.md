---
title: identity_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_providers
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
<tr><td><b>Name</b></td><td><code>identity_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.iam.identity_providers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="description" /> | `string` | A description of the identity provider. |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="display_name" /> | `string` | The human-readable name of the OAuth identity provider. |
| <CopyableCode code="issuer" /> | `string` | A publicly accessible URL uniquely identifying the OAuth<br />identity provider authorized to issue access tokens. |
| <CopyableCode code="jwks_uri" /> | `string` | A publicly accessible JSON Web Key Set (JWKS) URI for the OAuth<br />identity provider. JWKS provides a set of crypotgraphic keys<br />used to verify the authenticity and integrity of JSON Web<br />Tokens (JWTs) issued by the OAuth identity provider. |
| <CopyableCode code="keys" /> | `array` | The JWKS issued by the OAuth identity provider. Only `kid` (key ID)<br />and `alg` (algorithm) properties for each key set are included. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="state" /> | `string` | The current state of the identity provider. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_iam_v2identity_provider" /> | `SELECT` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to read an identity provider. |
| <CopyableCode code="list_iam_v2identity_providers" /> | `SELECT` |  | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Retrieve a sorted, filtered, paginated list of all identity providers. |
| <CopyableCode code="create_iam_v2identity_provider" /> | `INSERT` |  | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to create an identity provider. |
| <CopyableCode code="delete_iam_v2identity_provider" /> | `DELETE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to delete an identity provider. |
| <CopyableCode code="update_iam_v2identity_provider" /> | `UPDATE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to update an identity provider.<br /><br /> |
