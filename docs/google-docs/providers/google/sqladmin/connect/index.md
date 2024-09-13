---
title: connect
hide_title: false
hide_table_of_contents: false
keywords:
  - connect
  - sqladmin
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

Creates, updates, deletes, gets or lists a <code>connect</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connect</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.sqladmin.connect" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="backendType" /> | `string` | `SECOND_GEN`: Cloud SQL database instance. `EXTERNAL`: A database server that is not managed by Google. This property is read-only; use the `tier` property in the `settings` object to determine the database type. |
| <CopyableCode code="databaseVersion" /> | `string` | The database engine type and version. The `databaseVersion` field cannot be changed after instance creation. MySQL instances: `MYSQL_8_0`, `MYSQL_5_7` (default), or `MYSQL_5_6`. PostgreSQL instances: `POSTGRES_9_6`, `POSTGRES_10`, `POSTGRES_11`, `POSTGRES_12` (default), `POSTGRES_13`, or `POSTGRES_14`. SQL Server instances: `SQLSERVER_2017_STANDARD` (default), `SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`, `SQLSERVER_2019_STANDARD`, `SQLSERVER_2019_ENTERPRISE`, `SQLSERVER_2019_EXPRESS`, or `SQLSERVER_2019_WEB`. |
| <CopyableCode code="dnsName" /> | `string` | The dns name of the instance. |
| <CopyableCode code="ipAddresses" /> | `array` | The assigned IP addresses for the instance. |
| <CopyableCode code="kind" /> | `string` | This is always `sql#connectSettings`. |
| <CopyableCode code="pscEnabled" /> | `boolean` | Whether PSC connectivity is enabled for this instance. |
| <CopyableCode code="region" /> | `string` | The cloud region for the instance. For example, `us-central1`, `europe-west1`. The region cannot be changed after instance creation. |
| <CopyableCode code="serverCaCert" /> | `object` | SslCerts Resource |
| <CopyableCode code="serverCaMode" /> | `string` | Specify what type of CA is used for the server certificate. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instance, project" /> | Retrieves connect settings about a Cloud SQL instance. |
| <CopyableCode code="generate_ephemeral" /> | `EXEC` | <CopyableCode code="instance, project" /> | Generates a short-lived X509 certificate containing the provided public key and signed by a private key specific to the target instance. Users may use the certificate to authenticate as themselves when connecting to the database. |

## `SELECT` examples

Retrieves connect settings about a Cloud SQL instance.

```sql
SELECT
backendType,
databaseVersion,
dnsName,
ipAddresses,
kind,
pscEnabled,
region,
serverCaCert,
serverCaMode
FROM google.sqladmin.connect
WHERE instance = '{{ instance }}'
AND project = '{{ project }}'; 
```
