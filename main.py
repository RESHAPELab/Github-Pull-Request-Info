import src.auth as auth
import src.config as config
import src.gather as gather

if __name__ == "__main__":

    configs = config.get_configs()

    auth.Auth.setup(configs["general"]["accounts"], configs["general"]["rate-threshold"])
    result = gather.run(configs["args"], configs["gather"])

    

    print(result[2])
   