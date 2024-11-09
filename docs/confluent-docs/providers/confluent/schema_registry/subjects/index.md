---
title: subjects
hide_title: false
hide_table_of_contents: false
keywords:
  - subjects
  - schema_registry
  - azure
  - microsoft azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>subjects</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subjects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.schema_registry.subjects" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | Globally unique identifier of the schema |
| <CopyableCode code="metadata" /> | `object` | User-defined metadata |
| <CopyableCode code="references" /> | `array` | References to other schemas |
| <CopyableCode code="ruleSet" /> | `object` | Schema rule set |
| <CopyableCode code="schema" /> | `string` | Schema definition string |
| <CopyableCode code="schemaType" /> | `string` | Schema type |
| <CopyableCode code="subject" /> | `string` | Name of the subject |
| <CopyableCode code="version" /> | `integer` | Version number |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_schema_by_version" /> | `SELECT` | <CopyableCode code="subject, version" /> | Retrieves a specific version of the schema registered under this subject. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Retrieves a list of registered subjects matching specified parameters. |
| <CopyableCode code="delete_schema_version" /> | `DELETE` | <CopyableCode code="subject, version" /> | Deletes a specific version of the schema registered under this subject. This only deletes the version and the schema ID remains intact making it still possible to decode data using the schema ID. This API is recommended to be used only in development environments or under extreme circumstances where-in, its required to delete a previously registered schema for compatibility purposes or re-register previously registered schema. |
| <CopyableCode code="delete_subject" /> | `DELETE` | <CopyableCode code="subject" /> | Deletes the specified subject and its associated compatibility level if registered. It is recommended to use this API only when a topic needs to be recycled or in development environment. |
| <CopyableCode code="get_referenced_by" /> | `EXEC` | <CopyableCode code="subject, version" /> | Retrieves the IDs of schemas that reference the specified schema. |
| <CopyableCode code="get_schema_only_1" /> | `EXEC` | <CopyableCode code="subject, version" /> | Retrieves the schema for the specified version of this subject. Only the unescaped schema string is returned. |
| <CopyableCode code="look_up_schema_under_subject" /> | `EXEC` | <CopyableCode code="subject" /> | Check if a schema has already been registered under the specified subject. If so, this returns the schema string along with its globally unique identifier, its version under this subject and the subject name. |
| <CopyableCode code="register" /> | `EXEC` | <CopyableCode code="subject" /> | Register a new schema under the specified subject. If successfully registered, this returns the unique identifier of this schema in the registry. The returned identifier should be used to retrieve this schema from the schemas resource and is different from the schema's version which is associated with the subject. If the same schema is registered under a different subject, the same identifier will be returned. However, the version of the schema may be different under different subjects.
A schema should be compatible with the previously registered schema or schemas (if there are any) as per the configured compatibility level. The configured compatibility level can be obtained by issuing a GET http:get:: /config/(string: subject). If that returns null, then GET http:get:: /config
When there are multiple instances of Schema Registry running in the same cluster, the schema registration request will be forwarded to one of the instances designated as the primary. If the primary is not available, the client will get an error code indicating that the forwarding has failed. |

## `SELECT` examples

Retrieves a list of registered subjects matching specified parameters.


```sql
SELECT
id,
metadata,
references,
ruleSet,
schema,
schemaType,
subject,
version
FROM confluent.schema_registry.subjects
;
```
## `DELETE` example

Deletes the specified <code>subjects</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.schema_registry.subjects
WHERE subject = '{{ subject }}';
```
