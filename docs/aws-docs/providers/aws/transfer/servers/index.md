---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
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

Describes the properties of a file transfer protocol-enabled server that was specified.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Describes the properties of a file transfer protocol-enabled server that was specified.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.servers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="Arn" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="Certificate" /></td><td><code>Resource Type definition for AWS::Transfer::Certificate</code></td><td></td></tr>
<tr><td><CopyableCode code="ProtocolDetails" /></td><td><code> The protocol settings that are configured for your server. </code></td><td></td></tr>
<tr><td><CopyableCode code="Domain" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="EndpointDetails" /></td><td><code><p>The virtual private cloud (VPC) endpoint settings that are configured for your file transfer protocol-enabled server. With a VPC endpoint, you can restrict access to your server and resources only within your VPC. To control incoming internet traffic, invoke the <code>UpdateServer</code> API and attach an Elastic IP address to your server's endpoint.</p> <note> <p> After May 19, 2021, you won't be able to create a server using <code>EndpointType=VPC_ENDPOINT</code> in your Amazon Web Servicesaccount if your account hasn't already done so before May 19, 2021. If you have already created servers with <code>EndpointType=VPC_ENDPOINT</code> in your Amazon Web Servicesaccount on or before May 19, 2021, you will not be affected. After this date, use <code>EndpointType</code>=<code>VPC</code>.</p> <p>For more information, see https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#deprecate-vpc-endpoint.</p> </note></code></td><td></td></tr>
<tr><td><CopyableCode code="EndpointType" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="HostKeyFingerprint" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="IdentityProviderDetails" /></td><td><code>Returns information related to the type of user authentication that is in use for a file transfer protocol-enabled server's users. A server can have only one method of authentication.</code></td><td></td></tr>
<tr><td><CopyableCode code="IdentityProviderType" /></td><td><code><p>The mode of authentication for a server. The default value is <code>SERVICE_MANAGED</code>, which allows you to store and access user credentials within the Transfer Family service.</p> <p>Use <code>AWS_DIRECTORY_SERVICE</code> to provide access to Active Directory groups in Directory Service for Microsoft Active Directory or Microsoft Active Directory in your on-premises environment or in Amazon Web Services using AD Connector. This option also requires you to provide a Directory ID by using the <code>IdentityProviderDetails</code> parameter.</p> <p>Use the <code>API_GATEWAY</code> value to integrate with an identity provider of your choosing. The <code>API_GATEWAY</code> setting requires you to provide an Amazon API Gateway endpoint URL to call for authentication by using the <code>IdentityProviderDetails</code> parameter.</p> <p>Use the <code>AWS_LAMBDA</code> value to directly use an Lambda function as your identity provider. If you choose this value, you must specify the ARN for the Lambda function in the <code>Function</code> parameter for the <code>IdentityProviderDetails</code> data type.</p></code></td><td></td></tr>
<tr><td><CopyableCode code="LoggingRole" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="PostAuthenticationLoginBanner" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="PreAuthenticationLoginBanner" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="Protocols" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="S3StorageOptions" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="SecurityPolicyName" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="ServerId" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="State" /></td><td><code><p>Describes the condition of a file transfer protocol-enabled server with respect to its ability to perform file operations. There are six possible states: <code>OFFLINE</code>, <code>ONLINE</code>, <code>STARTING</code>, <code>STOPPING</code>, <code>START_FAILED</code>, and <code>STOP_FAILED</code>.</p> <p> <code>OFFLINE</code> indicates that the server exists, but that it is not available for file operations. <code>ONLINE</code> indicates that the server is available to perform file operations. <code>STARTING</code> indicates that the server's was instantiated, but the server is not yet available to perform file operations. Under normal conditions, it can take a couple of minutes for the server to be completely operational. Both <code>START_FAILED</code> and <code>STOP_FAILED</code> are error conditions.</p></code></td><td></td></tr>
<tr><td><CopyableCode code="Tags" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="UserCount" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="WorkflowDetails" /></td><td><code>Container for the <code>WorkflowDetail</code> data type. It is used by actions that trigger a workflow to begin execution.</code></td><td></td></tr>
<tr><td><CopyableCode code="StructuredLogDestinations" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="describe_server" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__ServerId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_servers" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="create_server" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_server" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__ServerId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_server" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__ServerId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="start_server" /></td>
    <td><code>EXEC</code></td>
    <td><CopyableCode code="data__ServerId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="stop_server" /></td>
    <td><code>EXEC</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>








