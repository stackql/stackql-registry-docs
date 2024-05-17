---
title: server
hide_title: false
hide_table_of_contents: false
keywords:
  - server
  - transfer
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Details of a Transfer family server

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Details of a Transfer family server</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.server" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="data___server_id" /></td><td><code>string</code></td><td>The server id</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Unique Amazon Resource Name (ARN) for the server.</td></tr>
<tr><td><CopyableCode code="certificate" /></td><td><code>string</code></td><td>The certificate of the server</td></tr>
<tr><td><CopyableCode code="domain" /></td><td><code>string</code></td><td>The domain of the server</td></tr>
<tr><td><CopyableCode code="endpoint_details" /></td><td><code>object</code></td><td>The virtual private cloud (VPC) endpoint settings that are configured for your file transfer protocol-enabled server. With a VPC endpoint, you can restrict access to your server and resources only within your VPC. To control incoming internet traffic, invoke the UpdateServer API and attach an Elastic IP address to your server's endpoint.</td></tr>
<tr><td><CopyableCode code="endpoint_type" /></td><td><code>string</code></td><td>The endpoint type of the server</td></tr>
<tr><td><CopyableCode code="host_key_fingerprint" /></td><td><code>string</code></td><td>The host key fingerprint of the server</td></tr>
<tr><td><CopyableCode code="identity_provider_details" /></td><td><code>object</code></td><td>Returns information related to the type of user authentication that is in use for a file transfer protocol-enabled server's users. A server can have only one method of authentication.</td></tr>
<tr><td><CopyableCode code="identity_provider_type" /></td><td><code>string</code></td><td>The mode of authentication for a server. The default</td></tr>
<tr><td><CopyableCode code="logging_role" /></td><td><code>string</code></td><td>The logging role of the server</td></tr>
<tr><td><CopyableCode code="post_authentication_login_banner" /></td><td><code>string</code></td><td>The post authentication login banner of the server</td></tr>
<tr><td><CopyableCode code="pre_authentication_login_banner" /></td><td><code>string</code></td><td>The pre authentication login banner of the server</td></tr>
<tr><td><CopyableCode code="protocol_details" /></td><td><code>object</code></td><td>The protocol settings that are configured for your server</td></tr>
<tr><td><CopyableCode code="protocols" /></td><td><code>array</code></td><td>The protocols of the server</td></tr>
<tr><td><CopyableCode code="s3_storage_options" /></td><td><code>object</code></td><td>The S3 storage options of the server</td></tr>
<tr><td><CopyableCode code="security_policy_name" /></td><td><code>string</code></td><td>The security policy name of the server</td></tr>
<tr><td><CopyableCode code="server_id" /></td><td><code>string</code></td><td>The server id</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>Describes the condition of a file transfer protocol-enabled server with respect to its ability to perform file operations. There are six possible states: OFFLINE, ONLINE, STARTING, STOPPING, START_FAILED, and STOP_FAILED. OFFLINE indicates that the server exists, but that it is not available for file operations. ONLINE indicates that the server is available to perform file operations. STARTING indicates that the server's was instantiated, but the server is not yet available to perform file operations. Under normal conditions, it can take a couple of minutes for the server to be completely operational. Both START_FAILED and STOP_FAILED are error conditions.</td></tr>
<tr><td><CopyableCode code="structured_log_destinations" /></td><td><code>array</code></td><td>The structured log destinations of the server</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags of the server</td></tr>
<tr><td><CopyableCode code="user_count" /></td><td><code>integer</code></td><td>The user count of the server</td></tr>
<tr><td><CopyableCode code="workflow_details" /></td><td><code>object</code></td><td>Container for the WorkflowDetail data type. It is used by actions that trigger a workflow to begin execution.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="view" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
data___server_id,
arn,
certificate,
domain,
endpoint_details,
endpoint_type,
host_key_fingerprint,
identity_provider_details,
identity_provider_type,
logging_role,
post_authentication_login_banner,
pre_authentication_login_banner,
protocol_details,
protocols,
s3_storage_options,
security_policy_name,
server_id,
state,
structured_log_destinations,
tags,
user_count,
workflow_details,
region
FROM aws.transfer.server
WHERE region = '<region>' AND data__ServerId = '<s-serverid>';
```





