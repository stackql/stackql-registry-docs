---
title: broker
hide_title: false
hide_table_of_contents: false
keywords:
  - broker
  - amazonmq
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>broker</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>broker</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.amazonmq.broker</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>SecurityGroups</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Configuration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>AuthenticationStrategy</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Users</code></td><td><code>array</code></td><td></td></tr><tr><td><code>SubnetIds</code></td><td><code>array</code></td><td></td></tr><tr><td><code>StompEndpoints</code></td><td><code>array</code></td><td></td></tr><tr><td><code>MqttEndpoints</code></td><td><code>array</code></td><td></td></tr><tr><td><code>AmqpEndpoints</code></td><td><code>array</code></td><td></td></tr><tr><td><code>DeploymentMode</code></td><td><code>string</code></td><td></td></tr><tr><td><code>EngineType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>EncryptionOptions</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr><tr><td><code>ConfigurationRevision</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>StorageType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>EngineVersion</code></td><td><code>string</code></td><td></td></tr><tr><td><code>MaintenanceWindowStartTime</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>HostInstanceType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AutoMinorVersionUpgrade</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>Logs</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ConfigurationId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>BrokerName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>WssEndpoints</code></td><td><code>array</code></td><td></td></tr><tr><td><code>IpAddresses</code></td><td><code>array</code></td><td></td></tr><tr><td><code>OpenWireEndpoints</code></td><td><code>array</code></td><td></td></tr><tr><td><code>LdapServerMetadata</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>PubliclyAccessible</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.amazonmq.broker
WHERE region = 'us-east-1' AND data__Identifier = '{Id}'
```
