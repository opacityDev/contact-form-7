if __name__=="__main__":
    import sys  
    file = open(".githooks/wp-config-docker.php","rt")
    content = file.read()
    final = content.replace("URL_TO_BE_CHANGED_WP_DOCKER",sys.argv[1])
    file.close()
    file = open("wp-config-docker.php","wt")
    file.write(final)
    file.close()
    exit(0)
